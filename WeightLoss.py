# Starting Out With Python 5th Edition: Chapter 4 - Exercise 11

MONTHS = 6 # Constant for diet plan of 6 months
POUNDS = 4 # At a reduced 500 calorie intake a day, there is an expected 4 lbs lost per month

# Input weight
weight = float(input('Enter your weight in pounds: '))

# Input validation
while weight <= 0:
    print('Weight cannot be negative or zero, try again.')
    weight = float(input('Enter your weight in pounds: '))

# Display heading
print('\nMonth\tProjected Weight at a 500')
print('       \tCalories Reduced Intake a Day')
print('--------------------------------------')
for month in range(MONTHS):
    weight -= 4
    print(f'{month + 1:<7d} {weight}lbs')