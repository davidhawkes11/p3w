# Code to instruct the computer to generate two random numbers, compares their values and displays output to the screen.
# Input: number1 and number2, both integer variables
# Output: the larger of the two integers, indicated as a comparison.
# The above text is commentary. The actual program starts below:

import random   # provides this program's access to the Python 3.5 builtin 'random'  module.
print ("Python 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_06.0d.4Challenge\n")
print ("A program to instruct the computer to generate two random numbers, compare their size\n and display output to the screen.\n" )
print ("The program will automatically generate two random number variables using the code\n 'numberX = random.randint(1, 100)'\n")


number1 = random.randint(1, 100)       # generates the first randomly generated number
print ("The first randomly generated value is:", number1)
number2 = random.randint(1, 100)       # generates the second randomly generated number
print ("The second randomly generated value is:", number2)

if number1 == number2:
    print("The two numbers are identical.")
elif number1 > number2:
    print ("Number 1, which is ", number1 ,", is greater than Number 2, which is",  number2 )
elif number1 < number2:
    print ("Number 1, which is ", number1 ,", is less than Number 2, which is",  number2 )    

print ("\nProgram successfully terminated." )

