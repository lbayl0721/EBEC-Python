"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 04/05/2022

Description:
    This program creates a quiz to test the user if they know the state capitals at random and tells them their score on the quiz.

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
from random import *

def main():
    """Write your mainline logic below this line (then delete this line)."""
    response = 1
    correct = 0
    incorrect = 0
    dictionary = get_state_data()                                                   #use function to get the dictionary
    while response != '0':
        state = choice(list(dictionary))                                            #get a state to quiz
        answer = dictionary[state].lower()
        response = input(f"What is the capital of {state} (enter 0 to quit)? ")     #get user response
        response = response.lower()
        if answer == response:                                                      #compare responses
            print("  That is correct!")
            del dictionary[state]
            correct += 1
        elif (answer != response) & (response != '0'):
            print("  That is incorrect.")
            print(f"  The capital of {state} is {answer.capitalize()}")
            incorrect += 1
        elif response == '0':
            print(f"You answered {correct} out of {correct + incorrect} questions correctly.")



def get_state_data():
    everything = []
    masterlist = {}
    with open("state_capitals.txt") as file:
        for line in file:
            everything.append(line.rstrip())                                        #get all state and capital data
        count = 0
        for i in everything:
            list = everything[count].split(',')
            key = (list[1])[1:]
            masterlist[key] = list[0]                                               #split data and assign into dictionary
            count += 1
        return masterlist
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
