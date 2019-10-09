# To print digit patterns
# For a given integer print the number of *'s that are equivalent to each digit in the integer.

def pattern(UserNumber):
    numbers = list(UserNumber)
    for number in numbers:
        number = int(number)
        print("|", end='')
        print(number * '*')

userNo = input('Enter your input: ')
pattern(userNo)