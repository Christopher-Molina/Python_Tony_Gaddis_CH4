# Starting Out With Python 5th Edition: Chapter 4 - Exercise 3

# Input amount budgeted for a month
budget = float(input('Amount budgeted this month: '))

# Initialize accumulator variable to 0
total = 0.0

# Input expense
n = 1
expense = float(input(f'\nEnter expense {n} or (0 to exit): '))

# Input validation loop
while expense != 0:
  n+=1
  total += expense # Add expense to accumulator variable
  expense = float(input(f'Enter expense {n} or (0 to exit): ')) # Input another expense
print()

# Determine if user is over budget, budget is equal to expenses, or is under budget
if budget > total:
  print(f'You have a ${budget:,.2f} budget and ${total:,.2f} expense this month. You\'re under budget.')
elif budget == total:
  print(f'You\'re budget and expenses are equal.')
else:
  print(f'You have a ${budget:,.2f} budget and ${total:,.2f} expense this month. You\'re over budget.')
