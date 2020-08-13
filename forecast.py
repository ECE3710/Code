import pandas as pd
import numpy as np
from pandas import DataFrame
from datetime import datetime, timedelta

caseData = pd.read_csv("../Data/case_count_ratio.csv")
mandateData = pd.read_csv('../Data/wikiData.csv')

# Returns date the stay at home order was issued
def stayAtHomeOrdered(state):
  stateMandates = mandateData.loc[mandateData['State'] == state]
  date = pd.to_datetime(stateMandates['Stay at Home Ordered']).to_numpy()[0]

  if not np.isnat(date):
    return date

# Returns data from the number (num) of days leading up to and including the date
def lastSevenDays(data, date, num=365):
  week = []

  for day in data.itertuples():
      week.append([day.date, day.cases])
      if (pd.to_datetime(day.date).to_numpy() == date):
        break
  if (num):
    return DataFrame(week, columns=['date', 'cases']).tail(num)

  return DataFrame(week, columns=['date', 'cases'])

# Returns weekly average for new cases
def newCasesWeeklyAvg(week):
  return round((week['cases'].values[6] - week['cases'].values[0]) / 7)

# Calculates the growth rate and multiplies it by the number of cases on the day the stay-at-home order was issued
def calcNewCasesPerDay(week):
  start = week['cases'].values[5]
  end = week['cases'].values[6]
  days = 1

  growthRate = np.log(end/start) / days
  return growthRate * week['cases'].values[6]

# Predicts the number of total cases if # of new cases per day equals the average of the # of new cases in the last 7 days
def forecastGrowth(state):
  stateData = caseData[caseData['state'] == state]
  today = pd.to_datetime(datetime.date(datetime.today())).to_numpy()
  date = stayAtHomeOrdered(state)
  if (date):
    week = lastSevenDays(stateData, date, 7)
    totalCases = week['cases'].values[-1]

    forecastedData = lastSevenDays(stateData, date)

    while (date != today):
      week = lastSevenDays(forecastedData, date, 7)
      # newCases = newCasesWeeklyAvg(week)
      newCases = round(calcNewCasesPerDay(week))
      totalCases += newCases

      row = pd.DataFrame([[date, totalCases]], columns = week.columns)
      forecastedData = forecastedData.append(row)
      date += np.timedelta64(1, 'D')

    forecastedData.to_csv(f'../Data/Forecasts/{state}_forecast.csv')