# Starting Out With Python 5th Edition: Chapter 4 - Exercise 10

# Constants for tuition increase in percentage and years
TUITION_INCREASE = 0.03
YEARS = 5

# Display headings
print('\nTuition before inflation is $8,000\n')
print('Year\tTuition Increase at 3%')

# Calculate projected tuition increase for the next 5 years
# Initialize starting tuition cost at $8,000
tuition_cost = 8000
for year in range(5):
    tuition_cost = tuition_cost + (tuition_cost * TUITION_INCREASE)
    print(f'{year+1:<7d} ${tuition_cost:,.2f}')
