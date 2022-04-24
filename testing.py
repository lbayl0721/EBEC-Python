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
    score = int(input("Enter a score: "))
    name = str(input("Enter player name: "))
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
    players = data[1::2]
    scores = data[0::2]
    players = [sub[1 :] for sub in players]
    print(scores)
    print(players)
    for i in scores:
        if i == '':
            scores.remove(i)
    if len(scores) > 0:
        scores = [int(i) for i in scores]
    
    count = 0
    if len(scores) == 0:
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
            print(players[i])
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        print("")
    elif score > scores[-1]:
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
        if len(scores) > 10:
            length = 10
        else:
            length = len(scores)
        for i in range(length):
            file.write(f'{scores[i]}, {players[i]}\n')
            print(players[i])
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        print("")
    elif score <= scores[-1] and len(scores) < 10:
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
            print(players[i])
        file.close()
        print(f"\nWay to go {name}!")
        print(f"You earned a total of {score} points and made it into the Hall of Fame!")
        print("")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
