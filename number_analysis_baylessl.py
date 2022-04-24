"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 07.2 - number analysis
Date: 03/24/2022

Description:
    this program accepts 10 input numbers and calculates the total, average, min, and max values

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
    print("Enter 10 numbers:")
    list = get_number_list()                                #use the get number list function to get the list
    maximum = max(list)                                     #calculate given parameters from the list
    minimum = min(list)
    total = sum(list)
    average = total/len(list)

    print(f"Highest number: {maximum:4.2f}")                #print values about the list
    print(f"Lowest number: {minimum:4.2f}")
    print(f"Total: {total:4.2f}")
    print(f"Average: {average:4.2f}")

def get_number_list():
    list = []
    for x in range(10):                                     #repeat ten times
        if x != 9:
            print("  number", end = '  ')
        else:
            print("  number", end = " ")
        print(x + 1, end = ' ')
        value = float(input("of 10: "))
        list.append(value)                                  #add new value to the list
    return list

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
