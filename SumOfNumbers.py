# Starting Out With Python 5th Edition: Chapter 4 - Exercise 8

number = int(input('Enter a positive number (negative to exit): '))

# Initialize accumulator
sum = 0
while number >= 0:
    sum += number # Add each iteration of number to sum
    number = int(input('Enter a positive number (negative to exit): '))

# Display sum
print('\nSum:', sum)