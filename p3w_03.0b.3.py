# Code to instruct the computer to calculate the five times table and display output to the screen
# The above text is commentary. The actual program starts below:
# Input: number, an integer variable
# Output: a vertical list of integers in the range specified in your range statement.

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity 3.0b3\n\n")
print ("A program to calculate the five times table and to display the output to the screen." )


print ("\n\nYou could solve this using a while loop:\n")
number = 1
while number  < 5:
    print(number, " x 5 = ", number * 5)
    number  = number + 1 #increments the counter

print("\n\nYou could also solve this using a range statement  for number in range (1, 5): \n")
for number in range (1, 5):
    print(number, " x 5 = ", number * 5)
print ("\n\nProgram successfully terminated." )




