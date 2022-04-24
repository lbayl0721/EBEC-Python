"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 09.2 - World Series
Date: 04/06/2022

Description:
    This program creates keys for all of the world series winners and how many times they have won. Any year can be searched for the winner

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


def main():
    """Write your mainline logic below this line (then delete this line)."""
    count_dictionary, year_dictionary = load_winners_data()                                     #get dictionaries
    year = int(input("Enter a year in the range 1903 -- 2021: "))
    if year < 1903 or year > 2021:
        print(f"  Data for the year {year} is not included in this system.")                    #weed out bad inputs
    elif year == 1904 or year == 1994:
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        winner = year_dictionary[year]                                                          #Get winner and the number of times they won
        count = count_dictionary[winner]
        print(f"  The {winner} won the World Series in {year}.")
        print(f"  They have won the World Series {count} times.")


def load_winners_data():
    everything = []
    winners_count = {}
    winners_year = {}
    with open("WorldSeriesWinners.txt") as file:
        for line in file:
            everything.append(line.rstrip())                                                     #get all the data
        winners_nodups = list(set(everything))
        count = 0
        for i in winners_nodups:
            winners_count[winners_nodups[count]] = everything.count(winners_nodups[count])      #find count of each unique winner
            count += 1
        year = 1903
        index = 0
        for i in everything:
            if year == 1904:
                year += 1
            if year == 1994:
                year += 1
            winners_year[year] = everything[index]                                              #assign year to each winner
            year += 1
            index += 1
    return winners_count, winners_year
    
        

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
