# Code to instruct the computer to generate two user's dice roll values and display output to the screen.
# Input: number, an integer variable
# Output: a vertical list of randomly generated integers in the range specified.
# The above text is commentary. The actual program starts below:

import random   # provides this program's access to the Python 3.5 builtin 'random'  module.
print ("Python 3.0 Workbook\nStudent Work Booklet\nStudent Activity p3w_05.0c.4Challenge\n")
print ("A program to instruct the computer to generate 100 dice roll values and display output to the screen.\n" )
print ("The program allows two users to enter a value for the preferred number of sides on the dice.\n" )
print ("This is best solved using a while loop:\n")

user1 = input("Who is the first player? ")          # asks for the name of user 1
user2 = input("Who is the second player? ")     # asks for the name of user 2

counter1 = 1                                          # initialises the pretest while loop to 1
counter2 = 2                                            # initialises the pretest while loop to 1
sides = int(input("Enter the number of sides you would like to have on the dice: "))
while counter1  <= 100:                       # sets the upper limit of the loop
    print(user1, "'s first dice roll ", counter1 ," is ", random.randint(1, sides) ," and ", user2 ,"'s dice roll", counter2 ,"is", random.randint(1, sides))    
    counter1  = counter1 + 1                    # increments the counter
    counter2  = counter2 + 1                    # increments the counter
print ("\nProgram successfully terminated." )

