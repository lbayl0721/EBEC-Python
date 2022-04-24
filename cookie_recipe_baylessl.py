"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/26/2022

Description:
    This program calculates the required ingredients to make an input number of cookies

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

    cookies = float(input("How many cookies do you want to make? ")) #This line receives the input number of cookies
    b = cookies/48*1.25 #perform butter calculation
    s = cookies/48*1.50 #perform sugar calculation
    f = cookies/48*2.50 #perform flour calculation
    c = "{:,.0f}".format(cookies) #format cookies value
    butter = format(b, '10,.2f') #format butter for printing
    sugar = format(s, '10,.2f') #format sugar
    flour = format(f, '10,.2f') #format flour

    print("To make", c,"cookies, you will need:")
    print(f"{butter} cups of butter")
    print(f"{sugar} cups of sugar")
    print(f"{flour} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
