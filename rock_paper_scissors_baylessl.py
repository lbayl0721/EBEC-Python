"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 03/09/2022

Description:
    This program uses the random module to create a game of rock paper scissors that the user can play.

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
from random import *                                                #import random module

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    computer = "rock"                                               #initialize choices
    player = "rock"
    while(computer == player):                                      #repeat while its a tie
        computer = get_computer_choice()                            #get computer and player choices
        player = get_player_choice()
        winner = get_winner(computer, player)                       #calculate winner
        if winner == "tie":                                         #print winner for all three options, repeat if necessary
            print(f"  The computer chose {computer}, and you chose {player}.")
            print("  Its a tie. Starting over.")
            print("")
        if winner == "computer":
            print(f"  The computer chose {computer}, and you chose {player}.")
            print(f"  {computer} beats {player}")
            print("  You lost.  Better luck next time.")
            print("Thanks for playing.") 
        if winner == "player":
            print(f"  The computer chose {computer}, and you chose {player}.")
            print(f"  {player} beats {computer}")
            print("  You won the game!")
            print("Thanks for playing.")            

    

def get_computer_choice():                                      #function to get computer choice
    options = ("rock","paper","scissors")
    computer = choice(options)
    return(computer)

def get_player_choice():                                         #function to get player choice and ensure it is correct
    player = input("Choose rock, paper, or scissors: ")
    while player != "rock" and player != "paper" and player != "scissors":
        print("You made an invalid choice. Please try again.")
        player = input("Choose rock, paper, or scissors: ")
    return(player)

def get_winner(option1, option2):                                 #function to chose the winner
    computer = option1
    player = option2
    rock = 0
    paper = 0
    scissors = 0
    if computer == player:
        winner = "tie"
    else:

        if computer == "rock" or player == "rock":
            rock = 1
        if computer == "paper" or player == "paper":
            paper = 1
        if computer == "scissors" or player == "scissors":
            scissors = 1
        if rock and scissors:
            if computer == "rock":
                winner = "computer"
            else:
                winner = "player"
        if scissors and paper:
            if computer == "scissors":
                winner = "computer"
            else:
                winner = "player"
        if paper and rock:
            if computer == "paper":
                winner = "computer"
            else:
                winner = "player"


    return(winner)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
