"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 03.4 - Organisms
Date: 02/20/2022

Description:
    This program predicts organism population growth based on starting size, growth rate, and days to grow

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


from time import time


def main():
    """Write your mainline logic below this line (then delete this line)."""
    start = float(input("Starting population, in thousands: ")) #get the input values
    percent = float(input("Average daily increase, in percent: "))
    time = int(input("Number of days to multiply: "))
    print("Day   Approx. Pop")

    for x in range(time + 1):                                   #loop to repeat for all days
        day = x
        population = start * (1+(percent/100)) ** day           #main calculation value
        daynum = "{:3.0f}".format(day)                          #printing and formatting
        popnum = format(population, '14,.3f')
        print(f"{daynum}{popnum}")
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
