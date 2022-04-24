"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 01.1 - Vineyard
Date: 01/26/22

Description:
    This program takes the input of post width, spacing, and total length to calculate and return the number of vines to be added

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

    print("Enter each of the following quantities in meters.")
    width = float(input("  How wide is the end-post assembly? ")) #This line receives the input width
    space = float(input("  How much space should be between the vines? ")) #this line receives the input space between vines
    length = float(input("  How long is this row? ")) # this line receives the input length of the full row

    vines=(length-2*width)//space
    #print(type(vines))
    print("\nThere is enough space for", int(vines), "vine(s) in this row.")             #This line prints output number of vines

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
