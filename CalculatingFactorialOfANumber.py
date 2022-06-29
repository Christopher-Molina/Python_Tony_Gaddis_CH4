# Starting Out With Python 5th Edition: Chapter 4 - Exercise 12

# Input a non-negative integer
integer = int(input('Enter a non-negative integer: '))

# Input validation
while integer < 0:
    print('Integer cannot be negative, try again.')
    integer = int(input('Enter a non-negative integer: '))

# The factorial of 0 or 1 is 1
if integer == 1 or integer == 0:
    print(f'{integer}! = 1')
    exit(0)

# Calculate its factorial
factorial = 1
print(f'\n{integer}! = ', end='')
for number in range(1, integer + 1):
    factorial *= number
    if number < integer:
        print(number, 'x', end=' ')
    else:
        print(number, '=', factorial)
