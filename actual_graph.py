from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def graphActual(state):
  data = pd.read_csv("../Data/case_count_ratio.csv")
  stateData = data.loc[data['state'] == state]
  
  dates = pd.to_datetime(stateData['date']).to_numpy()
  cases = stateData['cases'].to_numpy()

  x = dates
  y = cases

  plt.title(f'{state} Actual Cases')
  plt.plot_date(x, y, label='Actual cases')