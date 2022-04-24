"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 04.5 - Prime List
Date: 02/28/2022

Description:
    This program accepts an input number and prints all of the prime numbers up until that

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
    top = int(input("Enter a positive integer: "))              #get the input integer to test until
    prime_list = list((''))                                     #start the list of prime numbers
    for x in range (top + 1):
        prime = is_prime(x)                                     #test each number
        if prime:
            prime_list.append(x)                                #add prime numbers to the list
    print(f"The primes up to {top} are:", end = " ")
    print(*prime_list, sep = ", ")                              #print prime numbers

def is_prime(num):                                                      #prime testing function
    prime = False
    if num > 1:
        prime = True                                                        #default to true
        for i in range(2, int(num ** 0.5 + 1)):                                 #test until sqrt(num) to save time (autograder is impatient)
            if (num % i) == 0:
                prime = False
                break
    return bool(prime)                                                  #return the output, true for prime number
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
