"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 02/28/2022

Description:
    This program uses turtle graphics to draw a star pattern with a set number of points

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    side_length = 60
    points = int(input("Enter the number of points on the star: "))                                   #get input number of sides
    A = 360/points
    B = 2 * A
    right(90 - (B/2))
    fillcolor('pink')                                                                                  #start fill and initial angle
    begin_fill()
    for x in range(points):                                                                             #for loop to repeat for whole star
        forward(side_length)
        left(180 - A)
        forward(side_length)                                                                            #drawing and turning for one point on star
        right(180 - B)

    end_fill()

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
