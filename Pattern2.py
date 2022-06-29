# Starting Out With Python 5th Edition: Chapter 4 - Exercise 15

BASE_SIZE = 6

for row in range(BASE_SIZE):
    print('#', end='')
    for column in range(row):
        print(' ', end='')
    print('#')