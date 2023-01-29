# Starting Out With Python 5th Edition: Chapter 4 - Exercise 7

# Input number of days each penny will double
days = int(input('Enter number of days each penny will double: '))

# Input validation, days must be greater than or equal to 0
while days < 0:
  print('Error, a day cannot be zero or negative, try again.')
  days = int(input('Enter a day greater than zero and not negative: '))

# Initalize accumulator variable
earned = 0
for day in range(1, days + 1):
  if (day) == 1: # On day 1, you'll have 1 penny
     print(f'On day {day}, you\'ll earn 1 penny.')
     pennies = 1
     earned += pennies
  else: # Double the amount of pennies for the rest of the days
     pennies *= 2
     print(f'On day {day}, you\'ll earn {pennies:,.0f} pennies')
     earned += pennies # Add each doubled penny to earned salary

# Display total pay at the end of the period
print(f'\nTotal Earned: ${earned / 100:,.2f}')
