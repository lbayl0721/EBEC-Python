"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 04/13/2022

Description:
    This program reads and plots the data for cumulative covid cases in Indiana.

Contributors:
    None

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

import matplotlib.pyplot as plt                                                         #import ploting functions

def main():
    """Write your mainline logic below this line (then delete this line)."""
    everything = []
    splitdata = []
    dates = []
    cases = []
    with open("indiana_covid-19_data_spring_2022.txt") as file:                                 #open the text file
        for line in file:
            everything.append(line.rstrip())
    count = 0
    for i in everything:
        splitdata.append(everything[count].split())                                             #split the data into each date or case or test value
        count += 1
    data = [j for i in splitdata for j in i]
    dates = data[0::4]
    cases = data[2::4]                                                                          #separate dates and cases
    cases = [int(i) for i in cases]
    count = 0
    total_cases_thousand = []
    for i in cases:
        total_cases_thousand.append(sum(cases[0:count])/1000)                                   #calculate total positive tests
        count += 1
    fig, ax = plt.subplots() 
    ax.bar(dates, total_cases_thousand, width = 1)
    ax.set_title("Positive COVID-19 Cases in Indiana")
    ax.set_xlabel("Date")                                                                       #create the plot and show it
    ax.set_ylabel("Number of Cases (in thousands)")
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
