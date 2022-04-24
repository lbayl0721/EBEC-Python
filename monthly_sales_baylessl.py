"""
Author: Luke Bayless, baylessl@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 04/12/2022

Description:
    This program accepts sales values for each month and creates a pie chart to visualize them

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
import matplotlib.pyplot as plt                                                                 #import matplotlib

def main():
    """Write your mainline logic below this line (then delete this line)."""
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') #list of months
    sales = []                                                                                 #initialize the sales list
    for i in months:
        sales.append(int(input(f"Enter the sales for {i}: ")))                                 #get the sales values
    fig, ax = plt.subplots()                                                                   #initialize the plot
    c = ('#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A') #list of color codes
    ax.pie(sales, colors = c, labels = months)                                                 #create the pie chart
    ax.set_title('Monthly Sales Values')                                                       #add chart title and show
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
