"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 04/03/2022

Description:
    This program accepts a string input and switches it into pig latin and reprints it

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
    string = str(input("Enter a string: "))             #get input
    pig_latin = pig(string)                             #run function
    print("Pig latin:", pig_latin)                      #print pig latin

def pig(string):
    string = string.lower()             
    word_list = string.split()                          #split phrase into each word
    ending = 'ay'
    word_count = 0
    new_list = []
    for x in word_list:
        word = x
        new_word = word[1:] + word[0] + ending          #change each word
        new_list += [new_word]                          #add new word to pig lating phrase
        word_count += 1
    print(new_list)
    print(type(new_list))
    pig_latin = ' '.join(new_list)
    pig_latin = pig_latin.capitalize()
    return pig_latin
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
