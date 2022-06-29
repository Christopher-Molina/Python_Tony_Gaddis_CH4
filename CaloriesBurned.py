# Starting Out With Python 5th Edition: Chapter 4 - Exercise 2

# Initialize constant for calories burned per minute
CALORIES_PER_MINUTE = 4.2

# Display heading
print('Minute\tCalories Burned')
for minute in range(10, 31, 5):
 	  print(f'{minute} {minute * CALORIES_PER_MINUTE: 10.1f}')
