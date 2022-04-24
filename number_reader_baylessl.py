"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.5 - Number Reader
Date: 04/03/2022

Description:
    This program reads and analyzes the data in the random numbers text file and prints values about it

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
    list = []
    with open('random_numbers.txt') as file:                                    #open random numbers file
        for line in file:
            list.append(line.rstrip())                                          #make list without newline characters
        new_list = [int(i) for i in list]                                       #make list int for calculating
        count = len(new_list)
        minimum = int(min(new_list))
        maximum = int(max(new_list))  
        total = sum(new_list)
        average = total/count
    print(f"{count:,d} numbers were read from the file.")                      #print values
    print(f"Min: {minimum:,d}")
    print(f"Max: {maximum:,d}")
    print(f"Sum: {total:,d}")
    print(f"Avg: {average:,.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
