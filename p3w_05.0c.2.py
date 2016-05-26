# Code to instruct the computer to generate dice roll values and display output to the screen.
# Input: number, an integer variable
# Output: a vertical list of randomly generated integers in the range specified.
# The above text is commentary. The actual program starts below:

import random   # provides this program's access to the Python 3.5 builtin 'random'  module.
print ("Python 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_05.0c.2\n")
print ("A program to instruct the computer to generate 100 dice roll values of a 12 sided dice and display output to the screen.\n" )
print ("This is best solved using a while loop:\n")

counter = 1                                          # initialises the pretest while loop to 1
while counter  <= 100:                       # sets the upper limit of the loop
    print("Dice roll value", counter ," is ", random.randint(1, 12))    # prints the value to the screen
    counter  = counter + 1                    # increments the counter
print ("\nProgram successfully terminated." )

