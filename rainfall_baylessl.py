"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 03.3 - rainfall
Date: 02/17/2022

Description:
    This program calculates total and average rainfall per year for a given number of years

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
    total = 0
    years = int(input("Enter the number of years: "))                       #get the number of years
    if years <= 0:                                                          #catch bad input years
        print("Invalid input; years must be greater than 0.")
    else:
        for x in range(years):                                              #repeat loop for all years
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            print("  For year No.", x+1)
            for x in months:                                                #repeat loop for all months
                rainfall = float(input(f"    Enter the rainfall for {x}.: "))
                while(rainfall < 0):                                        #catch bad input rainfalls
                    print("    Invalid input; rainfall cannot be negative.")
                    rainfall = float(input(f"    Enter the rainfall for {x}.: "))
                total += rainfall
        count = years*12                                                    #formatting and printing statements
        average = total/count
        count = "{:,.0f}".format(count)
        average = "{:,.2f}".format(average)
        total = "{:,.2f}".format(total)
        print(f"There are {count} months.")
        print(f"The total rainfall was {total} inches.")
        print(f"The monthly average rainfall was {average} inches.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
