import pandas as pd
from plotnine import *

data = pd.read_csv("../Data/case_count_ratio.csv")

# Subsetting the dataframe

df = data[["date", "state", "Case/10,000", "Death/10,000"]]

dates = pd.to_datetime(df["date"]).to_numpy()

cases = df["Case/10,000"]

states = df["state"]

deaths = df["Death/10,000"]

case_ratio = ggplot(df, aes(x = dates, y = cases, color = states)) + geom_point()

death_ratio = ggplot(df, aes(x = dates, y = deaths, color = states)) + geom_point()

ggsave(case_ratio, "../Data/case_ratio_raw.png")
ggsave(death_ratio, "../Data/death_ratio_raw.png")
