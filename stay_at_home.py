from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../Data/wikiData.csv')

def stayAtHome(state):
  stateData = data.loc[data['State'] == state]

  ordered = pd.to_datetime(stateData['Stay at Home Ordered']).to_numpy()
  lifted = pd.to_datetime(stateData['Stay at Home Lifted']).to_numpy()

  plt.axvline(ordered, color='red', label='Stay at home ordered')
  plt.axvline(lifted, color='green', label='Stay at home lifted')