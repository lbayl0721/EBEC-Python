"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 04.2 - Maximum
Date: 02/27/22

Description:
    This program returns the maximum of two input values

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
    a = input("Enter the first integer: ")          #get the inputs
    b = input("Enter the second integer: ")
    c = max_of_two(a,b)                            #find the greater one
    print(f"The number {c} is greater.")            #Print the greater one

def max_of_two(a,b):                            #calculating function
    if int(a) > int(b):
        c = a
        
    else:
        c = b
    return c    
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
