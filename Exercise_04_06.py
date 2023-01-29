# Starting Out With Python 5th Edition: Chapter 4 - Exercise 6

# Formula: f = (9/5)C + 32
MIN = 0
MAX = 20

# Display heading
print('Celsius\t\tFahrenheit')
print('-----------------------')

# Calculate and display celsius converted to fahrenheit
for celsius in range(MIN, MAX + 1):
  if celsius < 10:
     print(f'{celsius}C {(9/5) * celsius + 32:14.2f}F')
  else:
     print(f'{celsius}C {(9/5) * celsius + 32:13.2f}F') # Format to display in a straight column
