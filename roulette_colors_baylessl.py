"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 02/02/2022

Description:
    This program takes an input number and returns its roulette color

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
    number = int(input("Please choose a pocket number: ")) #this line accepts the input number

    if number < 0 or number > 36: #checks for invalid inputs
        print("  Invalid Input!")
    elif number == 0:
        print(f"  Pocket number {number} is green.")
    elif (number > 0 and number <= 10) or (number > 18 and number <= 28): 
        if number % 2 == 0:
            print(f"  Pocket number {number} is black.")
        else:
            print(f"  Pocket number {number} is red.")
    elif (number > 10 and number <= 18) or (number > 18 and number <= 36): 
        if number % 2 == 0:
            print(f"  Pocket number {number} is red.")
        else:
            print(f"  Pocket number {number} is black.")
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
