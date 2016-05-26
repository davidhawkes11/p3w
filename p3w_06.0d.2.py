# Code to ask the user for their password and to respond with output.
# Input: a character string, entered in the clear (no echo masking available in IDLE).
# Output: a selected string response
# The above text is commentary. The actual program starts below:

print ("\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_06.0d.2\n\n")
print ("A program to ask the user for their password and to print a message.\n\n" )


pw = input("Please enter your password: \n")
if pw == "password":
    print("Welcome to the world\n")
elif pw != "password":
    print ("Access denied")

print("There is no password hiding facility from this interface.")
print ("Program successfully terminated.\n")



