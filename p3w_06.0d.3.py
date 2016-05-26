# Code to ask for user's two favourite numbers, to operate on them and to display the output to the screen.
# Input: two numbers, integer variables
# Output: the result of a mathematical operation on the two numbers
# The above text is commentary. The actual program starts below:

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_06.0d.3\n\n")
print ("A program to demonstrate string selection and to display the output to the screen.\n\n" )


number1 = int(input("What is your first favourite number? "))
number2 = int(input("What is your second favourite number? "))

menu = "What would you like to do with these two numbers? Enter 1, 2, 3, 4 or 9:\n\
       1. Add +\n\
       2. Subtract -\n\
       3. Multiply *\n\
       4. Divide /\n\
       9. Quit\n"

x = int(input(menu))
if x == 1:
    print("", number1 + number2)
elif x == 2:
        print("", number1- number2)
elif x == 3:
    print("", number1 * number2)
elif x ==  4:
    print("", number1 / number2)
elif x == 9:
    print("Goodbye!")




