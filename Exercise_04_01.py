# Starting Out With Python 5th Edition: Chapter 4 - Exercise 1

# Initialize constant for number of days
NUMBER_OF_DAYS = 5

# Accumulator variable
total = 0

for day in range(NUMBER_OF_DAYS):
    # Input number of bugs on current day
    bugs = int(input(f'How many bugs were encountered on day {day + 1}?'))
    total += bugs  # Add number of bugs to accumulator variable total

# Display total number of bugs encountered
print('\nTotal Bugs Encountered:', total)
