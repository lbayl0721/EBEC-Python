"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.4 - Number Writer
Date: 04/03/2022

Description:
    This program creates a file containing a specified number of a random numbers in a set range

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
from random import *                                                            #import random module

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    numbers = int(input("How many numbers would you like? "))
    with open('random_numbers.txt', 'w') as file:                                #create the file
        for x in range(numbers):
            value = str(randint(1019, 1215))                                    #get the new value
            file.write(value)                                                   #add value to the file
            file.write('\n')




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
