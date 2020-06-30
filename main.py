import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../Data/WHO-COVID-19-us-data.csv')

data.plot()
plt.show()