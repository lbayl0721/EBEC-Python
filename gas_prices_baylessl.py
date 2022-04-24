"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 04/12/2022

Description:
    This program reads a file containing the average gas prices in america in 2008 and plots it.

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
import matplotlib.pyplot as plt                                                 #import the plotting

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    prices = []
    with open('2008_Weekly_Gas_Averages.txt') as file:
        for line in file:
            prices.append(line.rstrip())                                        #add the prices from the text file
    prices = [float(i) for i in prices]
    #print(prices)
    
    fig, ax = plt.subplots()                                                    #create the plot
    ax.plot(prices)
    ax.grid()
    ax.set_title('2008 Weekly Gas Prices')
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')                             #Set the plot parameters
    ax.set_xlim(1, 52)
    ax.set_ylim(1.5, 4.25)
    plt.show()                                                                  #show the plot
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
