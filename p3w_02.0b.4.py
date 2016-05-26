# Using two or more numbers, create code to work out how to convert Celsius into Fahrenheit.
# The formula for converting Celsius to Fahrenheit is:
# deg C * 9/5 + 32 = deg F
# 
# Inputs: number1, number2
# Outputs: product of number 1 and number 2
# The above text is commentary. The actual program starts below:

print ("\n\n\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity 2.0b4\n\n")
print ("A program to allow the user to enter two or more numbers in degrees Celsius,\nthen convert the value from Celsius to Fahrenheit and show the result\n\n")

# First we define a function that accepts input in degrees Celsius and
# returns the ouput in degrees Fahrenheit

def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    print ("FLAG --> my function call is here, accepting  temp deg C and returning temp deg Fahrenheit ")
    return (T_in_celsius * 9 / 5) + 32

# Then we have a little main program that uses the fahrenheit function to do the conversion to Celsius.
# A little list of numbers in degrees Celsius
for t in (22.6, 25.8, 27.3, 29.8):
    print("Celsius", t, ": ", "Fahrenheit", fahrenheit(t))
    
