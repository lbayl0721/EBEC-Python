"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 05.4 - Purple Turtle
Date: 02/28/2022

Description:
    This program uses turtle graphics to draw the words purple turtle

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
    setup(600, 400)
    width(9)
    color("purple")


def draw_e():
    """Write this function."""
    setheading(0)
    penup()
    goto(60,30)
    left(90)
    pendown()
    circle(30, 300)
    penup()
    goto(0,30)
    pendown()
    setheading(0)
    forward(60)
    penup()
    goto(60,0)


def draw_l():
    """Write this function."""
    setheading(0)
    penup()
    goto(30,60)
    right(90)
    pendown()
    forward(60)
    penup()
    goto(60,0)

def draw_p():
    """Write this function."""
    setheading(0)
    left(90)
    pendown()
    forward(60)
    penup()
    setheading(0)
    goto(60,30)
    pendown()
    circle(30)
    penup()
    goto(60,0)


def draw_r():
    """Write this function."""
    setheading(0)
    
    goto(60,0)

def draw_t():
    """Write this function."""
    setheading(0)

    goto(60,0)

def draw_u():
    """Write this function."""
    setheading(0)

    goto(60,0)

def main():
    """After these lines, use your letter drawing functions
    to write code that will draw the words "purple turtle".
    """
    draw_e()

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
