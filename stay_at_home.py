from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../Data/wikiData.csv')

ordered = data['Stay at Home Ordered']
date_ordered = pd.to_datetime(ordered).to_numpy()
lifted = data['Stay at Home Lifted']
date_lifted = pd.to_datetime(lifted).to_numpy()
states = data['State'].to_numpy()

x1 = date_ordered
x2 = date_lifted
y = states

plt.plot_date(x1, y, color='red')
plt.plot_date(x2, y, color='green')
plt.gca().invert_yaxis()
plt.show()