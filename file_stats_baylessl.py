"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.3 - File Stats
Date: 04/03/2022

Description:
    This program runs through an input file and counts the words/lines then gives the average words per line

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
    with open('frontiero_v_richardson.txt') as file:                        #open file to get line count
        lines = file.readlines()
        line_count = len(lines)
    with open('frontiero_v_richardson.txt') as file:                        #open file again to get word count
        everything = file.read()
        words = everything.split()
        word_count = len(words)
        average = word_count/line_count                                     #calculate average words per line
        print("Total number of words:", word_count)
        print("Total number of lines:", line_count)
        print(f"Average number of words per line: {average:3.1f}")          #print the outputs
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
