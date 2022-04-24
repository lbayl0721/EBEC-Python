"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 02.1 - Leap Year
Date: 02/01/2022

Description:
    This program takes an input year and returns if it is a leap year, and also how many days February has for that year

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
    year = int(input("Enter a year: ")) #this line inputs the given year 

    if year % 100 == 0: #checks for divisibilty by 100
        if year % 400 == 0: #checks for divisibility by 400
            print (f"The year {year} is a leap year.") #leap year output
            print (f"February of {year} has 29 days.")
        else:
            print (f"The year {year} is not a leap year.") #non leap year output
            print(f"February of {year} has 28 days.")
    elif year % 4 == 0: #checks for divisibility by 4
        print (f"The year {year} is a leap year.") # leap year output
        print (f"February of {year} has 29 days.")
    else:
        print (f"The year {year} is not a leap year.") #catch all output if year is not divisible by any of the above values
        print(f"February of {year} has 28 days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
