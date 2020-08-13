"""

Building a csv file that looks at ratio of cases to population for a more
accurate comparison of cases of COVID-19 across the US

Garrett Matthews

"""

import csv
import pandas as pd


def case_rat():
    """Function to run this whole script"""

    # Reading case data by county from NYTimes Github using pandas

    url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

    df = pd.read_csv(url, error_bad_lines=False)

    # Getting the column names as a list
    col_name = df.columns.tolist()

    # Converted to a list because the functionality I had built prior to using pandas revolved around lists

    case = df.values.tolist()
    case.insert(0, col_name)

    # Opening the population data - see github for source location and how it was edited

    population = open('../Data/us_pop_statexcounty.csv', 'r')

    # Dictionary to contain FIPS ID and the Population estimate
    pop_dict = {}

    pop = []

    # Making the population CSV into a list, dropping the first line (headers), and removing the \n character

    for line in population:
        pop_temp = []
        for i in line.split(','):
            pop_temp.append(i)
        pop.append(pop_temp)

    # print(pop)
    for i in range(len(pop)):
        pop[i] = [x.replace('\n', '') for x in pop[i]]

    # print(pop)

    for i in range(len(pop)):
        if i == 0:
            pass
        else:
            pop_dict[float(pop[i][0])] = int(pop[i][-1])

    # Adding a cases per 10,000 population / county

    for i in range(len(case)):
        fips = case[i][2]
        if i == 0:
            case[i].append("Case/10,000")
            case[i].append("Death/10,000")
        else:
            if pd.isnull(fips):
                # This is to prevent errors from missing FIPS values in the source data
                case[i].append('NULL')
                case[i].append('NULL')
            else:
                county_pop = pop_dict[fips]
                ratio = county_pop/10000
                if ratio == 0:
                    case_ratio = "NULL"
                    death_ratio = "NULL"
                else:
                    case_ratio = int(case[i][3]) / ratio
                    death_ratio = int(case[i][4]) / ratio
                case[i].append(case_ratio)
                case[i].append(death_ratio)

    return case


def regions(case):
    """Function to add a region to each state"""
    region = {"Washington": "West", "Oregon": "West", "California": "West", "Nevada": "West", "Idaho": "West",
              "Montana": "West", "Wyoming": "West", "Utah": "West", "Colorado": "West", "Arizona": "Southwest",
              "New Mexico": "Southwest", "Texas": "Southwest", "Oklahoma": "Southwest", "Arkansas": "Southeast",
              "Louisiana": "Southeast", "Mississippi": "Southeast", "Alabama": "Southeast", "Florida": "Southeast",
              "Georgia": "Southeast", "South Carolina": "Southeast", "North Carolina": "Southeast",
              "Tennessee": "Southeast", "Kentucky": "Southeast", "West Virginia": "Southeast", "Virginia": "Southeast",
              "North Dakota": "Midwest", "South Dakota": "Midwest", "Nebraska": "Midwest", "Kansas": "Midwest",
              "Minnesota": "Midwest", "Iowa": "Midwest", "Missouri": "Midwest", "Wisconsin": "Midwest",
              "Illinois": "Midwest", "Michigan": "Midwest", "Indiana": "Midwest", "Ohio": "Midwest",
              "Maryland": "Northeast", "Pennsylvania": "Northeast", "Delaware": "Northeast", "New Jersey": "Northeast",
              "New York": "Northeast", "Connecticut": "Northeast", "Massachusetts": "Northeast",
              "Rhode Island": "Northeast", "Vermont": "Northeast", "New Hampshire": "Northeast", "Maine": "Northeast",
              "Alaska": "Unconnected", "Hawaii": "Unconnected", "Guam": "Unconnected", "Puerto Rico": "Unconnected",
              "Virgin Islands": "Unconnected", "Northern Mariana Islands": "Unconnected",
              "District of Columbia": "Northeast"}

    # Adding the regions to the data list
    for i in range(len(case)):
        if i == 0:
            case[i].append("Region")
        else:
            case[i].append(region[case[i][1]])

    return case


def write_regions(case):
    """Breaks the list into each region and sends the list to be written to a csv"""
    west = []
    southwest = []
    midwest = []
    southeast = []
    unconnected = []
    northeast = []
    for i in range(len(case)):
        if i == 0:
            west.append(case[i])
            southwest.append(case[i])
            southeast.append(case[i])
            northeast.append(case[i])
            midwest.append(case[i])
            unconnected.append(case[i])
        if case[i][-1] == "West":
            west.append(case[i])
        elif case[i][-1] == "Southwest":
            southwest.append(case[i])
        elif case[i][-1] == "Midwest":
            midwest.append(case[i])
        elif case[i][-1] == "Southeast":
            southeast.append(case[i])
        elif case[i][-1] == "Northeast":
            northeast.append(case[i])
        elif case[i][-1] == "Unconnected":
            unconnected.append(case[i])

    write_out(west, '../Data/west_ratio.csv')
    write_out(southeast, '../Data/southeast_ratio.csv')
    write_out(southwest, '../Data/southwest_ratio.csv')
    write_out(northeast, '../Data/northeast_ratio.csv')
    write_out(unconnected, '../Data/unconnected_ratio.csv')
    write_out(midwest, '../Data/midwest_ratio.csv')


def write_out(case,file_name):
    """Writes out the list to a CSV file"""
    file = open(file_name, 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(case)


def main():
    lyst = case_rat()
    case = regions(lyst)
    write_regions(case)
    write_out(case, '../Data/case_count_ratio.csv')


if __name__ == "__main__":
    main()
