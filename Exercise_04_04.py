# Starting Out With Python 5th Edition: Chapter 4 - Exercise 4

# Formula: distance = speed x time
# Input speed of vehicle in miles per hour
speed = int(input('Enter speed of vehicle in miles per hour: '))

# Input number of hours the vehicle has traveled
hours = int(input('Enter number of hours vehicle has traveled: '))

# Display heading
print('\nHour\t\tDistance Traveled')
print('-----------------------------')

# Calculate and display distance traveled per hour
for hour in range(hours):
   print(f'{hour + 1} {hour * speed:14.1f}')
print()