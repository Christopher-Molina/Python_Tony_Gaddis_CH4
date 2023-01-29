# Starting Out With Python 5th Edition: Chapter 4 - Exercise 9

# Constant for mm the ocean level rises yearly
MM_PER_YEAR = 1.6

# Constant for max number of years to determine
MAX_YEAR = 25

# Display header
print('Year    Ocean Level in Mm')
print('-------------------------')

# Calculate mm the ocean level will rise for the next 25 years if it rises by 1.6 mm per year
for year in range(1, MAX_YEAR + 1):
    if year < 10:
        print(f'{year} {year * MM_PER_YEAR:21.2f}mm')
    else:
        print(f'{year} {year * MM_PER_YEAR:20.2f}mm')
