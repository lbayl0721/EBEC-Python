"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 03.1 Arrows
Date: 02/15/2022

Description:
    This program draws growing arrows based on an input number of total arrows

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
    num = int(input("Enter the number of arrows to draw: ")) #get the input number of arrows to draw
    for x in range(num): #loop through all arrows
        print("<", end = '')
        for y in range(x): #create arrow length
            print("=", end = '')
        print(">")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
