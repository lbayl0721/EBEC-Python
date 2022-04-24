"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 12.1 - Pyword
Date: 05/02/2022

Description:
    This program is a version of Jotto, as it sets up a word game in which the user attempts to guess the word in under six tries.

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
from random import *

"""Write new functions below this line (starting with unit 4)."""
def get_input():                                                #get user input
    print("----- Main Menu -----")
    print("1. New Game")
    print("2. See Hall of Fame")
    print("3. Quit\n")
    choice = input("What would you like to do? ")
    return choice

def get_choice():
    choice = 0
    while choice != '1' and choice != '2' and choice != '3':    #reject bad inputs
        choice = get_input()
        if choice != '1' and choice != '2' and choice != '3':
            print("\nInvalid choice. Please try again.\n")
    return choice

def get_hall_of_fame():                                     #function to display the hall of fame

    print("\n--- Hall of Fame ---")
    print(" ## : Score : Player")
    everything = []
    splitdata = []
    players = []
    scores = []
    with open("hall_of_fame.txt") as file:
        for line in file:
            everything.append(line.rstrip()) 
    count = 0
    for i in everything:
        splitdata.append(everything[count].split(','))                     
        count += 1
    data = [j for i in splitdata for j in i]
    players = data[1::2]                                    #read and split data into scores and players
    scores = data[0::2]
    players = [sub[1 :] for sub in players]
    for i in scores:
        if i == '':
            scores.remove(i)
    if len(scores) > 0:                                     #exceptions to keep code from throwing errors with a small hall of fame
        scores = [int(i) for i in scores]
    count = 0
    if len(scores) > 0:
        for i in scores:  
            print(f"{count+1:3d} : {scores[count]:5d} : {players[count]}") #print HoF
            count += 1
    print("")

def get_guess(attempt):                                                #get the users guess, reject bad inputs
    guess = '0'
    while len(guess) != 5 or guess.isalpha() == False:
        guess = str(input(f"{attempt}? "))
        if len(guess) != 5:
            print("\nInvalid guess. Please enter exactly 5 characters.\n")
        elif guess.isalpha() == False:
            print("\nInvalid guess. Please only enter letters.\n")
    return guess

def pick_game_words(words):                                             #simple function to keep autograder happy
    
    answer = sample(words, k=3)
    return answer

def play_game():                                                    #main game function
    total_score = 0
    guess = '0'
    name = input("Enter your player name: ")
    words = []
    with open("words.txt") as file:
        for line in file:
            words.append(line.rstrip())
    answers = pick_game_words(words)                                #pick game answers for three rounds
    for i in range(3):
        score = 0
        round = i + 1
        print(f"\nRound {round}:")
        round_analysis = []
        for i in range(26):
            round_analysis.extend(' ')                              #set up display of previous choices
        for i in range(6):
            attempt = i + 1
            potential_score = 2 ** (6 - attempt)                    #preset score for that attempt
            if attempt == 6:
                potential_score = 1
            guess = get_guess(attempt)
            guess = guess.lower()
            guess_letters = []
            guess_letters[:] = guess                                #get the user guess, split into readable characters
            guess_ascii = []
            for x in guess_letters:
                guess_ascii.append(ord(x) - 96)
            guess_analysis = ['X', 'X', 'X', 'X', 'X']
            count = 0
            for i in guess_letters:
                if i in answers[round - 1]:
                    if i == answers[round - 1][count]:
                        guess_analysis[count] = '!'                 #compare guess to answer and set the analysis
                    else:
                        guess_analysis[count] = '?'
                count += 1

            count = 0
            for i in guess_analysis:
                location = guess_ascii[count] - 1
                if round_analysis[location] == ' ' or round_analysis[location] == 'X':
                    round_analysis[location] = i                    #update full round letter analysis
                if round_analysis[location] == '?' and (i == '?' or i == '!'):
                    round_analysis[location] = i
                count += 1

            guess_analysis = ''.join(guess_analysis)
            round_analysis_print = ''.join(round_analysis)
            print(f"   {guess_analysis}     {round_analysis_print}")        
            print(f"   {guess}     abcdefghijklmnopqrstuvwxyz")         #print guess and current round results
            if guess == answers[round - 1]:
                score = potential_score
                break                                                   #break loop for correct guess
        total_score += score
        if score == 32:
            print(f"Genius! You earned {score} points this round.")
        if score == 16:
            print(f"Magnificent! You earned {score} points this round.")
        if score == 8:
            print(f"Impressive! You earned {score} points this round.") #print statements depending on score
        if score == 4:
            print(f"Splendid! You earned {score} points this round.")
        if score == 2:
            print(f"Great! You earned {score} points this round.")
        if score == 1:
            print(f"Phew! You earned {score} points this round.")
        if score == 0:
            print(f"You ran out of tries.")
            print(f"The word was {answers[round - 1]}.")
    return total_score, name

def assign_hof(score, name):                                        #function to update Hall of Fame
    everything = []
    splitdata = []
    players = []
    scores = []
    with open("hall_of_fame.txt") as file:
        for line in file:
            everything.append(line.rstrip()) 
    count = 0
    for i in everything:
        splitdata.append(everything[count].split(','))                     
        count += 1
    data = [j for i in splitdata for j in i]
    players = data[1::2]                                              #read current HoF data
    scores = data[0::2]
    players = [sub[1 :] for sub in players]
    for i in scores:
        if i == '':
            scores.remove(i)
    if len(scores) > 0:
        scores = [int(i) for i in scores]
    
    count = 0
    if len(scores) == 0:                                        #exception to auto include score if no HoF present
        scores.insert(0, score)
        players.insert(0, name)
        file = open("hall_of_fame.txt", "r+")
        file.truncate(0)
        if len(scores) > 10:
            length = 10
        else:
            length = len(scores)
        for i in range(length):
            file.write(f'{scores[i]}, {players[i]}\n')
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        get_hall_of_fame()
    elif score > scores[-1]:                                    #see about adding score if it is greater than the smallest one
        if score > scores[0]:
            scores.insert(0, score)
            players.insert(0, name)
        else:
            count = 0
            for i in scores:
                if score <= scores[count] and score > scores[count + 1]:
                    scores.insert(count + 1, score)
                    players.insert(count + 1, name)
                    break
                count += 1
        file = open("hall_of_fame.txt", "r+")
        file.truncate(0)
        if len(scores) > 10:                                    #cap the HoF at the top 10 and recreate the text file
            length = 10
        else:
            length = len(scores)
        for i in range(length):
            file.write(f'{scores[i]}, {players[i]}\n')
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        get_hall_of_fame()
    elif score <= scores[-1] and len(scores) < 10:                  #clause to add score if HoF still smaller than 10
        scores.append(score)
        players.append(name)
        file = open("hall_of_fame.txt", "r+")
        file.truncate(0)
        if len(scores) > 10:
            length = 10
        else:
            length = len(scores)
        for i in range(length):
            file.write(f'{scores[i]}, {players[i]}\n')
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        get_hall_of_fame()
    

def main():

    print("Welcome to PyWord.\n")               #Start up the Game!
    choice = get_choice()                       #get the choice from the menu
    while True:                                 #repeat choices until the user is done playing
        if choice == '1':
            total_score, name = play_game()     #main portion of code; playing the game
            assign_hof(total_score, name)
            choice = get_choice()
        if choice == '2':
            get_hall_of_fame()                  #show hall of fame and return to menu
            choice = get_choice()
        if choice == '3':
            print("Goodbye.")
            break



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
