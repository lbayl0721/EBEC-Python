"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 02/14/2022

Description:
    This program takes an input number of seconds and converts to days, hours, minutes, etc.

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
    time = int(input("Please enter a time in seconds: ")) #this line gets the input time in seconds
    days = time // 86400 #these lines do all the calculations
    hours = time % 86400 // 3600
    minutes = time % 3600 // 60
    seconds = time % 60
    total = "{:,}".format(time)

    print(f"  {total} seconds", end = ' ') #these lines create the ouput print statements
    if time >= 60:
        print('equals', end = '')
        if days:
            print(f' {days} day(s)', end = '')
        if hours:
            if days:
                if minutes or seconds:      #nested if statements to determine inclusion of "and" in the output
                    print(',', end ='')
                else:
                    print(' and', end = '')
            print(f' {hours} hour(s)', end = '')
        if minutes:
            if days or hours:
                if seconds:
                    print(',', end = '')
                else:
                    print(' and', end = '')
            print(f' {minutes} minute(s)', end = '')
        if seconds:
            if days or hours or minutes:
                print(' and', end = '') 
            print(f' {seconds} second(s)', end = '')
    else:
        print('is less than one minute', end = '')
    print('.')
    
    
    
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
