# Code to instruct the computer to count to 100 and display output to the screen
# Input: number, an integer variable
# Output: a vertical list of integers in the range specified in your range statement.
# The above text is commentary. The actual program starts below:

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity 3.0b4\n\n")
print ("A program to calculate the five times table and to display the output to the screen." )


print ("\n\nYou could solve this using a while loop:\n")
number = 1
while number  <= 100:               # sets the upper limit of the loop
    print(number)                           # prints the value to the screen
    number  = number + 1            # increments the counter

print("\n\nYou could also solve this using a range statement  for numbers in range (1, 101): \n")
for number in range (1, 101):   # sets the lower and upper limit of the range
    print(number)                           # prints the curent value to the screen and increments the counter
print ("\n\nProgram successfully terminated." )

