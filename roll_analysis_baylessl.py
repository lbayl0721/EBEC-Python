"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 03/25/2022

Description:
    This program calculates the roll frequency of d6 dice

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


def main():
    """Write your mainline logic below this line (then delete this line)."""
    print("Roll  Frequency")
    list = get_2d6_rolls(1000000)                           #get list of dice rolls
    total = len(list)
    two = list.count(2)             
    two_prob = two/total                                    #get probability of set number 
    print(f"  2{two_prob:10.2%}")                           #print probability
    three = list.count(3)
    three_prob = three/total
    print(f"  3{three_prob:10.2%}")
    four = list.count(4)
    four_prob = four/total
    print(f"  4{four_prob:10.2%}")
    five = list.count(5)
    five_prob = five/total
    print(f"  5{five_prob:10.2%}")
    six = list.count(6)
    six_prob = six/total
    print(f"  6{six_prob:10.2%}")
    seven = list.count(7)
    seven_prob = seven/total
    print(f"  7{seven_prob:10.2%}")
    eight = list.count(8)
    eight_prob = eight/total
    print(f"  8{eight_prob:10.2%}")
    nine = list.count(9)
    nine_prob = nine/total
    print(f"  9{nine_prob:10.2%}")
    ten = list.count(10)
    ten_prob = ten/total
    print(f" 10{ten_prob:10.2%}")
    eleven = list.count(11)
    eleven_prob = eleven/total
    print(f" 11{eleven_prob:10.2%}")
    twelve = list.count(12)
    twelve_prob = twelve/total
    print(f" 12{twelve_prob:10.2%}")


def roll_d6():                                              #function to get random dice roll
    roll = randint(1, 6)
    return roll

def get_2d6_rolls(rolls):                                   #function to create list of two random dice rolled a set number of times
    list = []
    for x in range(rolls):
        roll1 = roll_d6()
        roll2 = roll_d6()
        roll = roll1 + roll2
        list.append(roll)
    return(list)



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
