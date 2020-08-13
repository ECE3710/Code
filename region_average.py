"""

Python script to get averages for each region to serve as a master graph

"""

import statistics
import csv


def main():
    """Main function to make this code callable"""
    # Reading in the data and getting it ready to work with
    file = open("../Data/case_count_ratio.csv", 'r')
    case = []

    for line in file:
        case_temp = []
        for i in line.split(','):
            case_temp.append(i)
        case.append(case_temp)

    for i in range(len(case)):
        case[i] = [x.replace('\n', '') for x in case[i]]
    # Creating the sub dictionaries for the separated data
    west = {}
    southwest = {}
    southeast = {}
    midwest = {}
    northeast = {}
    unconnected = {}
    # Putting the case and death ratios for in the separate dictionaries as Date: [[Case, Death], ..]
    for i in range(len(case)):
        if case[i][-1] == "West":
            if case[i][0] in west:
                west[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                west[case[i][0]] = temp
        elif case[i][-1] == "Southwest":
            if case[i][0] in southwest:
                southwest[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                southwest[case[i][0]] = temp
        elif case[i][-1] == "Southeast":
            if case[i][0] in southeast:
                southeast[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                southeast[case[i][0]] = temp
        elif case[i][-1] == "Midwest":
            if case[i][0] in midwest:
                midwest[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                midwest[case[i][0]] = temp
        elif case[i][-1] == "Northeast":
            if case[i][0] in northeast:
                northeast[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                northeast[case[i][0]] = temp
        elif case[i][-1] == "Unconnected":
            if case[i][0] in unconnected:
                unconnected[case[i][0]].append([float(case[i][5]), float(case[i][6])])
            else:
                lyst = [float(case[i][5]), float(case[i][6])]
                temp = [lyst]
                unconnected[case[i][0]] = temp
    # Making a nested dictionary with {Region : region_dictionary}
    master = {"West": west, "Southwest": southwest, "Southeast": southeast, "Midwest": midwest,
              "Northeast": northeast, "Unconnected": unconnected}
    # Created a copy just in case
    copy = master.copy()
    # Taking the average of each date for each region and replacing the list of cases and deaths with
    # a list of the averages
    for i in copy:
        for j in copy[i]:
            cases = []
            death = []
            for k in copy[i][j]:
                cases.append(k[0])
                death.append(k[1])
            case_average = statistics.mean(cases)
            death_average = statistics.mean(death)
            copy[i][j] = [[case_average, death_average]]
    # List for the headers
    lyst = [["Region", "Date", "Average Case/10,000", "Average Death/10,000"]]
    # Formatting the data into a nested list for ease of CSV writing
    for i in copy:
        for j in copy[i]:
            for k in copy[i][j]:
                lyst.append([i, j, k[0], k[1]])
    # Writing the data out as a csv
    with open("../Data/region_average.csv", "w+", newline= '') as file:
        write = csv.writer(file)
        write.writerows(lyst)


if __name__ == "__main__":
    main()
