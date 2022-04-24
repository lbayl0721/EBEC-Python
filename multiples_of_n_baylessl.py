"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 07.1 - multiples of n
Date: -3/24/2022

Description:
    This program returns a list and then only the items in the list that are a multiple of a set integer

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
    list = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]        #list to be tested
    multiples = multiples_of(13, list)                                          #run the function of the test
    print("Original list of numbers:")
    print(f"  {list}")
    print("Numbers in the list that are multiples of 13:")                      #print statements
    print(f"  {multiples}")

def multiples_of(integer, list):
    multiples = []                                                              #function to find the multiples
    length = len(list)
    for x in range(length):
        if list[x] % integer == 0:                                              #main calculation to see if it is a multiple
            multiples.append(list[x])
    return multiples
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
