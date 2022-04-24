"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 03/08/2022

Description:
    This program creates a random math quiz and return if the right number was entered

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
from random import *                                        #import random library

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    num1 = random_number(2)                                 #run random number function for two and three digit numbers
    num2 = random_number(3)
    answer = num1 + num2                                    #calculate the right answer
    print("  ",num1)
    print("+",num2)
    print("-----")
    response = int(input("= "))                             #get the input response
    if response == answer:
        print("Correct -- Good Work!")
    else:
        print("Incorrect. The correct answer is ", answer, ".", sep = "")       #print the answer depending on right or wrong

def random_number(digits):
    if digits == 2:
        num = randint(10,99)
    if digits == 3:
        num = randint(100,999)
    return(num)
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
