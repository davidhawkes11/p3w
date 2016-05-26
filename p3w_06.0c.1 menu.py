# Code to demonstrate string selection and to display the output to the screen.
# Input: number, an integer variable
# Output: a selected string response
# The above text is commentary. The actual program starts below:

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_06.0b.1\n\n")
print ("A program to demonstrate string selection and to display the output to the screen.\n\n" )

menu = "What would you like?:\n\
    1. A complement?\n\
    2. An insult?\n\
    3. A proverb?\n\
    4. An idiom?\n\
    9. Quit\n"

x = int(input(menu))
if x == 1:
    print("You look lovely today!")
elif x == 2:
    print("You smell funny")
elif x == 3:
    print("Two wrongs don't make a right, but three lefts do...")
elif x ==  4:
    print("The pen is mightier than the sword")
elif x == 9:
    print("Goodbye!")




