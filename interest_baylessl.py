"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 01.2 - Interest
Date: 01/26/2022

Description:
    This program inputs interest parameters and calculates the future account balance after an input number of years

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

    print("Enter the following parameters.")
    P = float(input("  The initial deposit? ")) #This line receives the input deposit
    r = float(input("  The annual interest rate in percent? ")) #this line receives the input interest rate
    t = float(input("  The number of years the account earn interest? ")) # this line receives the input future account age
    n = float(input("  The number of times interest is compounded each year: ")) # this line receives the input interest compounding

    FV = P*(1+(r/100)/n)**(n*t)
    Balance = format(FV, '10,.2f')
    print(f"The balance of this account will be ${Balance} after {t} years.")             #This line prints output number of vines


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
