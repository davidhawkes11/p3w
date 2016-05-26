# Code to instruct the computer to generate dice roll values and display output to the screen.
# Input: number, an integer variable
# Output: a vertical list of randomly generated integers in the range specified.
# The above text is commentary. The actual program starts below:

import random   # provides this program's access to the Python 3.5 builtin 'random'  module.
print ("Python 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_05.0c.3Challenge\n")
print ("A program to instruct the computer to generate 100 dice roll values and display output to the screen.\n" )
print ("The program allows the user to enter a value for the preferred number of sides on the dice.\n" )
print ("This is best solved using a while loop:\n")

counter = 1                                          # initialises the pretest while loop to 1
sides = int(input("Enter the number of sides you would like to have on the dice: "))
while counter  <= 100:                       # sets the upper limit of the loop
    print("The first dice roll ", counter ," is ", random.randint(1, sides))
    counter  = counter + 1                    # increments the counter
print ("\nProgram successfully terminated." )

