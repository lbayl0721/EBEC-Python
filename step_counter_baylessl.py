"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 08.6 - Step Counter
Date: 04/04/2022

Description:
    This program reads and analyzes a text file that contains information on number of steps taken per day.

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
    print("The average steps taken each month were:")
    steps = []
    with open('steps.txt') as file:                                             #Open the steps file
        for line in file:
            steps.append(line.rstrip())
        january = steps[0:31]
        february = steps[31:59]
        march = steps[59:90]
        april = steps[90:120]
        may = steps[120:151]
        june = steps[151:181]                                                   #get the indices for each month
        july = steps[181:212]
        august = steps[212:243]
        september = steps[243:273]
        october = steps[273:304]
        november = steps[304:334]
        december = steps[334:365]
        january_average = sum([int(i) for i in january])/31                     #calculate the average for the month
        print("January".rjust(10),":", f"{january_average:6.2f}")               #format and print the output
        february_average = sum([int(i) for i in february])/28                   #repeat for each month
        print("February".rjust(10),":", f"{february_average:6.2f}")
        march_average = sum([int(i) for i in march])/31
        print("March".rjust(10),":", f"{march_average:6.2f}")
        april_average = sum([int (i) for i in april])/30
        print("April".rjust(10),":", f"{april_average:6.2f}")
        may_average = sum([int (i) for i in may])/31
        print("May".rjust(10),":", f"{may_average:6.2f}")
        june_average = sum([int (i) for i in june])/30
        print("June".rjust(10),":", f"{june_average:6.2f}")
        july_average = sum([int (i) for i in july])/31
        print("July".rjust(10),":", f"{july_average:6.2f}")
        august_average = sum([int (i) for i in august])/31
        print("August".rjust(10),":", f"{august_average:6.2f}")
        september_average = sum([int (i) for i in september])/30
        print("September".rjust(10),":", f"{september_average:6.2f}")
        october_average = sum([int (i) for i in october])/31
        print("October".rjust(10),":", f"{october_average:6.2f}")
        november_average = sum([int (i) for i in november])/30
        print("November".rjust(10),":", f"{november_average:6.2f}")
        december_average = sum([int (i) for i in december])/31
        print("December".rjust(10),":", f"{december_average:6.2f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
