# Code that asks the user for two numbers and to display the output to the screen.
# Input: two numbers, an integer variable
# Output: larger of the two numbers entered
# The above text is commentary. The actual program starts below:

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_06.0d.1\n\n")
print ("A program that to ask the user for two numbers, to compare them and")
print("to display the output to the screen.\n\n")


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if (n1 == n2):
     print("The two numbers are identical")
elif (n1 > n2):
        print("The first number ",  n1 ,"is larger than the second number ", n2)
elif (n1 < n2):
        print("The first number ", n1 ," is smaller than the second number ", n2)
print("Goodbye!")
print("\nProgram successfully terminated.")
