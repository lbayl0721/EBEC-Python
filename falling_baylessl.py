"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 04.1 - Falling
Date: 02/24/2021

Description:
    This program calculates the fall of an object every five seconds on the surface of venus.

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
    print("Time (s)  Distance (m)")             #initial print statements
    print("----------------------")
    for t in range(5, 51, 5):                   #loop for all times
        d = falling_dist(t)
        time = format(t, '8.0f')
        dist = format(d, '14.1f')
        print(f"{time}{dist}")

def falling_dist(t):                            #function to repeat calculations
    d = 0.5*8.87*t**2
    return(d)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
