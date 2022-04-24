"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.2 - Phone number converter
Date: 04/03/2022

Description:
    This program converts phone numbers that use letters into the actual numbers

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
    string = str(input("Enter a telephone number: "))                       #get input phone number
    new_number = convert_number(string)                                     #run the converter function
    print("The phone number is", new_number)                                #print new number

def convert_number(string):
    sets = string.split('-')                                                #split number into each grouping
    new_list = []
    for y in sets:
        clump = []
        for x in y:
            if x == 'A' or x == 'B' or x == 'C' or x == 'a' or x == 'b' or x == 'c':        #adjust the letters to numbers
                x = '2'
            elif x == 'D' or x == 'E' or x == 'F' or x == 'd' or x == 'e' or x == 'f':
                x = '3'
            elif x == 'G' or x == 'H' or x == 'I' or x == 'g' or x == 'h' or x == 'i':
                x = '4'
            elif x == 'J' or x == 'K' or x == 'L' or x == 'j' or x == 'k' or x == 'l':
                x = '5'
            elif x == 'M' or x == 'N' or x == 'O' or x == 'm' or x == 'n' or x == 'o':
                x = '6'
            elif x == 'P' or x == 'Q' or x == 'R' or x == 'S' or x == 'p' or x == 'q' or x == 'r' or x == 's':
                x = '7'
            elif x == 'T' or x == 'U' or x == 'V' or x == 't' or x == 'u' or x == 'v':
                x = '8'
            elif x == 'W' or x == 'X' or x == 'Y' or x == 'Z' or x == 'w' or x == 'x' or x == 'y' or x == 'z':
                x = '9'
            
            clump += [x]
        grouping = ''.join(clump)
        new_list += [grouping]
    phone_number = '-'.join(new_list)                                                           #recreate list
    return phone_number

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
