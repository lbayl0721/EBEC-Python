"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 02/14/2022

Description:
    This program calculates the reynolds number for the fluid flow based on input information

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

    temp = int(input("Enter the temperature in \u00B0C as 5, 20, or 50: ")) #input values for T, V, and D
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    diameter = float(input("Enter the pipe's diameter (m): "))
    if temp == 5:                                                           #set the corresponding viscosity
        viscosity = 1.52E-06
    if temp == 20:
        viscosity = 1.00E-06
    if temp == 50:
        viscosity = 5.54E-07
    reynold = (velocity*diameter)/viscosity                                 #calculate reynolds number for printing
    temp = "{:,.1f}".format(temp)
    print(f"At {temp}\u00B0C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe is %3.2e." % (reynold))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
