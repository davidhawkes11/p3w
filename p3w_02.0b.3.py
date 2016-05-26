# Create code to accept two numbers (of type integer) and multiply them together:
# number1
# number2
# 
# Inputs: number1, number2
# Outputs: product of number 1 and number 2
# The above text is commentary. The actual program starts below:

print ("\n\n\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity 2.0b5Challenge\n\n")
print ("A program to discount prices" )

# First we accept the two input numbers from the user and confirm that we have them:
#Error trapping is needed here in case the user enters a real or floating point number or a letter!


while True:
        try:
                fullprice = float(input("Please enter your full price: $ "))
                break
        except ValueError:
                print("Not a valid price! Please try again ...")
print ("Great, you successfully entered your price!")

while True:
        try:
                discount = float(input("Please enter your percentage discount as an integer in range 0-100: "))
                break
        except ValueError:
                print("Not a valid discount! Please try again ...")
print ("Great, you successfully entered your discount!")

print ("Discounted price = $", fullprice - (fullprice * discount/100))
print ("Program successfully terminated.")


