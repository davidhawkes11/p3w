# Code to prompt for two numbers.
# Input:    Two numbers, 
# Output:   Result of the division in format x remainder y
# The above text is commentary. The actual program starts below:

import math
print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_08.0b.1\n\n")
print ("Two numbers, division in format x remainder y and to display the output to the screen.\n\n" )

# Menu setup: user selects a value of 1, 4 or 9
menu = "What would you like to do?:\n\
       1. Find the division and remainder.\n\
       9. Quit\n"

# Menu: based on selection above

menuselection = int(input(menu))
if menuselection == 1:                                                      # if 1 is entered, prompt for the 2 other sides
    number1 = int(input("first number: \n"))
    number2 = int(input("second number:  \n"))
    remainder = int(number1 % number2)                  # '#' is a modulus symbol to calculate integer division
    print ("result is ", int((number1/number2)), "remainder", remainder)

elif menuselection == 2:                                                    # if 2 is entered, prompt for hypotenuse and side1
    hypotenuse = int(input("Length of hypotenuse = "))
    side1 = int(input("Length of side 1 = "))
    side2 = int(math.sqrt((hypotenuse**2)-(side1**2)))
    print ("Length of side 2 = ", side2)
elif menuselection == 9:                                                    # if 9 is entered, print goodbye message and exit.
    print("Goodbye!")

print ("Program successfully terminated.")
