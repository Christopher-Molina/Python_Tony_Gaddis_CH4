# Starting Out With Python 5th Edition: Chapter 4 - Exercise 5

# Input the number of years
years = int(input('Enter the number of years: '))

# Initialize constant for number of months
MONTHS_IN_YEAR = 12

# Initialize accumulator variable for total rainfall
total = 0.0

for year in range(years):
  print()
  for month in range(MONTHS_IN_YEAR):
     if (month + 1) == 1:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for January in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 2:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for February in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 3:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for March in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 4:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for April in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 5:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for May in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 6:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for June in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 7:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for July in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 8:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for August in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 9:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for September in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 10:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for October in year {year + 1}: '))
        total += inches_of_rainfall
     elif (month + 1) == 11:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for November in year {year + 1}: '))
        total += inches_of_rainfall
     else:
        inches_of_rainfall = float(input(f'Enter inches of rainfall for December in year {year + 1}: '))
        total += inches_of_rainfall

# Calculate and display the total number of months of the entire period
# and display total inches of rainfall
total_months = MONTHS_IN_YEAR * years
print(f'\nTotal Months: {total_months}')
print(f'Total Inches of Ranfall: {total:.2f}')
