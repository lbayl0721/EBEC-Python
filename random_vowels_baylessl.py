"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/21/2022

Description:
    This program creates a module and functions to print five vowels in a random order on turtle graphics

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
from vowels import *
from random import *


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    vowels = ["a", "e", "i", "o", "u"]
    order = sample(vowels, 5)
    print(order)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
