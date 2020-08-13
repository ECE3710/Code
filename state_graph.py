import pandas as pd
from plotnine import *


def graph(region, file_name):
    """
    Creates a case graph and death graph for each submitted region
    For the file name, only include the beginning - ie 'west', the rest will be added
    """
    df = region[["date", "state", "Case/10,000", "Death/10,000", "Region"]]
    dates = pd.to_datetime(df["date"]).to_numpy()
    cases = df["Case/10,000"]
    deaths = df["Death/10,000"]
    states = df["state"]

    case_ratio = ggplot(df, aes(x = dates, y = cases, color = states)) + geom_point() +\
        ggtitle("Cases/10,000 - Region: " + file_name.capitalize())

    death_ratio = ggplot(df, aes(x = dates, y = deaths, color = states)) + geom_point() +\
        ggtitle("Deaths/10,000 - Region: " + file_name.capitalize())

    case_name = "../Data/" + file_name + "_case.png"
    death_name = "../Data/" + file_name + "_death.png"

    ggsave(case_ratio, case_name)
    ggsave(death_ratio, death_name)


def main():
    west = pd.read_csv("../Data/west_ratio.csv")
    southwest = pd.read_csv("../Data/southwest_ratio.csv")
    southeast = pd.read_csv("../Data/southeast_ratio.csv")
    midwest = pd.read_csv("../Data/midwest_ratio.csv")
    northeast = pd.read_csv("../Data/northeast_ratio.csv")
    unconnected = pd.read_csv("../Data/unconnected_ratio.csv")

    graph(west, "west")
    graph(southeast, "southeast")
    graph(southwest, "southwest")
    graph(midwest, "midwest")
    graph(northeast, "northeast")
    graph(unconnected, "unconnected")

    reg = pd.read_csv("../Data/region_average.csv")
    date = pd.to_datetime(reg["Date"]).to_numpy()
    regions = reg["Region"]
    cases = reg["Average Case/10,000"]
    deaths = reg["Average Death/10,000"]

    case_average = ggplot(reg, aes(x = date, y= cases, color = regions)) + geom_point()
    death_average = ggplot(reg, aes(x = date, y = deaths, color = regions)) + geom_point()

    ggsave(case_average, "../Data/case_average.png")
    ggsave(death_average, "../Data/death_average.png")


if __name__ == "__main__":
    main()