# Starting Out With Python 5th Edition: Chapter 4 - Exercise 14

BASE_SIZE = 7

for row in range(BASE_SIZE):
    for column in range(BASE_SIZE, row, -1): # Column will be assigned the range of row for each iteration
        print('*', end='')
    print()
