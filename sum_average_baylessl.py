"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 03.2 - Sum Average
Date: 02/15/2022

Description:
    This program calculates the sum and average for an input set of numbers

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
    new = 0
    sum = 0
    average = 0
    count = 0
    while new >= 0:                             #loop to repeat while positive numbers are entered
        new = float(input("Enter a non-negative number (negative to quit): ")) #get the input
        if new >= 0:
            count = count + 1
            sum = sum + new
            average = sum/count
    if count == 0:
        print("  You didn't enter any numbers.")                #in case there are no positive inputs
    else:
        total = "{:,.3f}".format(sum)
        avg = "{:,.3f}".format(average)
        num = int(count)
        print(f"  You entered {num} numbers.")                  #formatting and printing
        print(f"  Their sum is {total} and their average is {avg}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
