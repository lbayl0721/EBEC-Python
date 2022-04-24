"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 09.3 - Course Info
Date: 04/06/2022

Description:
    This program creates nested dictionaries that contain information regarding fake classes.

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
    course_data = get_course_data()                                                          #get course info
    course = str(input("Enter a course number: "))
    if course in course_data:                                                                #check for valid input
        print(f"  The details for course {course} are:")
        print(f"    Instructor: {course_data[course]['instructor']}")                          #print course info
        print(f"          Room: {course_data[course]['room']}")
        print(f"          Time: {course_data[course]['time']}")
    else:
        print(f"  {course} is an invalid course number.")

def get_course_data():
    dict_101 = {'room' : '3004', 'instructor' : 'Django', 'time' : '9:00 a.m.'}
    dict_102 = {'room' : '4501', 'instructor' : 'Idle', 'time' : '10:00 a.m.'}                  #set up dictionaries
    dict_103 = {'room' : '6755', 'instructor' : 'Rich', 'time' : '11:00 a.m.'}
    dict_110 = {'room' : '1244', 'instructor' : 'Marshal', 'time' : '12:00 p.m.'}
    dict_241 = {'room' : '1411', 'instructor' : 'Pickle', 'time' : '2:00 p.m.'}  
    course_data = {'CS101' : dict_101, 'CS102' : dict_102, 'CS103' : dict_103, 'NT110' : dict_110, 'CM241' : dict_241}
    return course_data
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
