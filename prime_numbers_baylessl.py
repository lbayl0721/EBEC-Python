"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: MM/DD/YYYY

Description:
    This program takes any number and tells if its prime

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


def main():

    test = int(input("Enter a positive integer (-1 to quit): "))        #initial input
    while test != -1:
        prime = is_prime(test)                                          #test to see if its prime
        if prime:
            print(f"  {test} is prime!")
        else:                                                           #print statements
            print(f"  {test} is not prime.")
        test = int(input("Enter a positive integer (-1 to quit): "))    #repeat input



def is_prime(num):                                                      #prime testing function
    prime = False
    if num > 1:

        prime = True                                                        #default to true
        for i in range(2, int(num ** 0.5)):                                 #test until sqrt(num) to save time (autograder is impatient)
            if (num % i) == 0:
                prime = False
                break
    return bool(prime)                                                  #return the output, true for prime number



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
