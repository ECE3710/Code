"""

Building a csv file that looks at ratio of cases to population for a more
accurate comparison of cases of COVID-19 across the US

Garrett Matthews

"""
# Turning this script into a function to allow for easier call from separate scripts


def case_rat():
    """Function to run this whole script"""

    # Importing libraries

    import csv
    import pandas as pd

    # Reading case data by county from NYTimes Github using pandas

    url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

    df = pd.read_csv(url, error_bad_lines=False)

    # Converted to a list because the functionality I had built prior to using pandas revolved around lists

    case = df.values.tolist()

    # Opening the population data - see github for source location and how it was edited

    population = open('../Data/us_pop_statexcounty.csv', 'r')

    # Dictionary to contain FIPS ID and the Population estimate
    pop_dict = {}

    population = population.readlines()[1:]
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

    for i in pop:
        pop_dict[float(i[0])] = int(i[-1])

    # print(pop_dict)

    # Following the above steps to make the case counts into a list
    # This was for an earlier version when I was reading the data from my desktop
    # Rather than using pandas to take it directly from the github source
    """
    case = []

    for line in case_data:
        case_temp = []
        for i in line.split(','):
            case_temp.append(i)
        case.append(case_temp)

    # print(case)
    for i in range(len(case)):
        case[i] = [x.replace('\n', '') for x in case[i]]
    """
    # print(case[0:5])

    # Making a dictionary of FIPS : {County : State}

    fips_dict = {}

    for i in pop:
        county_state = {i[2]: i[1]}
        fips_dict[i[0]] = county_state

    # print(fips_dict)

    # Adding a cases per 10,000 population / county

    case_copy = case.copy()

    for i in range(len(case)):
        fips = case[i][3]
        if pd.isnull(fips):
            # This is to prevent errors from missing FIPS values in the source data
            case[i].append('NULL')
            case[i].append('NULL')
        else:
            county_pop = pop_dict[fips]
            ratio = county_pop/10000
            case_ratio = int(case[i][4]) / ratio
            death_ratio = int(case[i][5]) / ratio
            case[i].append(case_ratio)
            case[i].append(death_ratio)

    # Writing the edited Case Counts data to a new CSV file

    file = open('../Data/case_count_ratio.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(case)


def main():
    case_rat()


if __name__ == "__main__":
    main()
