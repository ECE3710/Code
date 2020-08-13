import matplotlib.pyplot as plt
import pandas as pd

from forecast import forecastGrowth
from forecast_graph import graphForecast
from actual_graph import graphActual
from stay_at_home import stayAtHome

statesData = pd.read_csv('../Data/states.csv')
states = statesData['name']

for state in states:
  forecastGrowth(state)
  graphForecast(state)
  graphActual(state)
  stayAtHome(state)
  plt.legend()
  plt.savefig(f'../Data/Graphs/{state}_graph.png')
  plt.clf()