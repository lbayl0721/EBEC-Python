"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 00.1 - Hello User
Date: MM/DD/YYYY

Description:
    This program receives an input user name and returns a hello message with their name and an exclamation mark.

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

    name = input("What is your name? ") #This line receives the input name
    print(f"Hello {name}!")             #This line prints the hello response with the input name

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
