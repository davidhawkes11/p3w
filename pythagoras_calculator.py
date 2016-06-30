# pythagorean_triangle_checker.py
# Program uses a number of functions to calculate if a combination of numbers forms
# a right angled triangle


def get_triangle_sides():
    sides = []
    print("Type the length of each side.")
    while len(sides) != 3:
        side_length = input('> ')
        if side_length.isdigit() == True and int(side_length) != 0:
            sides.append(int(side_length))
        else:
            print("Not a proper length. Try again.\n")

    hypotenuse = max(sides)
    c = hypotenuse
    sides.remove(c)
    a = sides[0]
    b = sides[1]

    triple = '(' + str(a) + ',' + str(b) + ',' + str(c) + ')'

    if a**2 + b**2 == c**2:
        print('\nTriple ' + triple + " does form a Pythagorean triangle.")
    elif a**2 + b**2 != c**2:
        print('\nTriple ' + triple + " does not form a Pythagorean triangle.")


def ask_question():
    question = "\nType 'q' to quit, or hit <Enter> to try again."
    print(question)
    new_value = 0
    while not new_value:
        ans = input('> ')
        if ans == '':
            print()
        elif ans == 'q':
            new_value = -1
        else:
            print('Wrong answer.')
            print(question)
            continue
        return new_value


def main():
    print('{0:^80}'.format('WELCOME to PYTHAGOREAN TRIANGLE CHECKER\n'))
    value = 0
    while value != -1:
        get_triangle_sides()
        value = ask_question()
    print('Goodbye!')


if __name__ == '__main__': main()
