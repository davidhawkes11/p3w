# Code to use Pythagoras' theorem.
# Input: number, an integer variable, part of a Pythagorean triple
# Output: hypotenuse or another side
# The above text is commentary. The actual program starts below:

import math
print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_08.0a.1\n\n")
print ("A program to use Pythagoras' theorem and to display the output to the screen.\n\n" )
print ("PYTHAGORAS CALCULATOR")

# Menu setup: user selects a value of 1, 4 or 9
menu = "What would you like to do?:\n\
       1. Find the hypotenuse of a Pythagorean right angled triangle.\n\
       2. Find another side of a Pythagorean right angled triangle.\n\
       9. Exit\n"

# Menu: based on selection above
menuselection = int(input(menu))
if menuselection == 1:                                                      # if 1 is entered, prompt for the 2 other sides
    side1 = int(input("Length of first side: \n"))
    side2 = int(input("Length of second side:  \n"))
    hypotenuse = int(math.sqrt((side1**2) + (side2**2)))
    print("\nHypotenuse is equal to: ", hypotenuse)
elif menuselection == 2:                                                    # if 2 is entered, prompt for hypotenuse and side1
    hypotenuse = int(input("Length of hypotenuse = "))
    side1 = int(input("Length of side 1 = "))
    side2 = int(math.sqrt((hypotenuse**2)-(side1**2)))
    print ("Length of side 2 = ", side2)
elif menuselection == 9:                                                    # if 9 is entered, print goodbye message and exit.
    print("Goodbye!")

print ("Program successfully terminated.")
