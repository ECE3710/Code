from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import os

def graphForecast(state):
  if os.path.exists(f'../Data/Forecasts/{state}_forecast.csv'):
    data = pd.read_csv(f'../Data/Forecasts/{state}_forecast.csv')
    
    dates = pd.to_datetime(data['date']).to_numpy()
    cases = data['cases'].to_numpy()

    x = dates
    y = cases

    plt.title(f'{state} Forecasted Cases')
    plt.plot_date(x, y, label='Predicted cases')

graphForecast('Arkansas')