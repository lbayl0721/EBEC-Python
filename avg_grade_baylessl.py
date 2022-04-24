"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 02/28/2022

Description:
    This program takes input grades and calculates the average and letter grade

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

    a = get_valid_score()                                       #get the input values
    a_grade = determine_grade(a)
    a_print = format(a, '.1f')
    print(f"  The letter grade for {a_print} is {a_grade}.")    #print value and letter grade
    b = get_valid_score()
    b_grade = determine_grade(b)
    b_print = format(b, '.1f')
    print(f"  The letter grade for {b_print} is {b_grade}.")
    c = get_valid_score()
    c_grade = determine_grade(c)
    c_print = format(c, '.1f')
    print(f"  The letter grade for {c_print} is {c_grade}.")
    d = get_valid_score()
    d_grade = determine_grade(d)
    d_print = format(d, '.1f')
    print(f"  The letter grade for {d_print} is {d_grade}.")
    e = get_valid_score()
    e_grade = determine_grade(e)
    e_print = format(e, '.1f')
    print(f"  The letter grade for {e_print} is {e_grade}.")

    print("")
    list = [a, b, c, d, e]
    average = calc_average(list)                                #final print statements for averages
    avg_grade = determine_grade(average)
    average = format(average, '.2f')
    print("Results:")
    print(f"  The average score is {average}.")
    print(f"  The letter grade for {average} is {avg_grade}.")


def get_valid_score():                                          #function to ensure input values are valid
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    return score

def calc_average(list):                                         #function to accept any list of any size and find its average
    count = float(len(list))
    average = (float(sum(list)))/count
    return average

def determine_grade(num):                                       #function to calculate lettter grade
    if num >= 92:
        grade = "A"   
    elif num < 92 and num >= 82:
        grade = "B"
    elif num < 82 and num >= 73:
        grade = "C"
    elif num <73 and num >= 64:
        grade = "D"
    else:
        grade = "F"
    return grade


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
