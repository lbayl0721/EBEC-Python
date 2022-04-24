"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/1/2022

Description:
    This program calculates cost and discount for an input number of purchases.

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
    packages = int(input("How many packages will be purchased: ")) #this line accepts the input packages purchased
    
    if packages < 0:
        print("  Invalid Input!") #catches invalid inputs
    elif packages < 4: 
        print("  No discount applied.") 
        price = packages * 880 #price calculation 
        dollars = "${:,.2f}".format(price) #format cost
        print(f"  The total price to purchase {packages} packages is {dollars}.") #print cost
    elif packages < 40: 
        print ("  10% discount applied.") 
        price = (packages *880) * 0.9 
        dollars = "${:,.2f}".format(price) 
        print(f"  The total price to purchase {packages} packages is {dollars}.") 
    elif packages < 200: 
        print("  15% discount applied.") 
        price = (packages * 880) * 0.85  
        dollars = "${:,.2f}".format(price) 
        print(f"  The total price to purchase {packages} packages is {dollars}.") 
    elif packages < 1000: 
        print("  30% discount applied.") 
        price = (packages * 880) * 0.7 
        dollars = "${:,.2f}".format(price) 
        print(f"  The total price to purchase {packages} packages is {dollars}.") 
    else: #price calculation for large purches of 1000+
        print("  42% discount applied.") 
        price = (packages * 880) * 0.58 
        dollars = "${:,.2f}".format(price) 
        print(f"  The total price to purchase {packages} packages is {dollars}.") 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
