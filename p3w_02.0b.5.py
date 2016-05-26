# Create code to accept a price and give a discount.
# Includes error trapping for incorrect input.
# 
# Inputs: fullprice, discount
# Outputs: discounted price
# The above text is commentary. The actual program starts below:

print ("\n\n\n\n\nPython 3.0 Workbook\nStudent Work Booklet\nStudent Activity 2.0b5Challenge\n\n")
print ("A program to discount prices" )

while True:
        try:
                fullprice = float(input("Please enter your full price > $0.00: $ "))
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


