# Starting Out With Python 5th Edition: Chapter 4 - Exercise 13

# Input starting number of organisms
organisms = int(input('Starting number of organisms: '))

# Input validation
while organisms < 0:
    print('Enter a non-negative number, try again.')
    organisms = int(input('Starting number of organisms: '))

# Input average daily increase
increase = int(input('\nAverage daily increase (as a percentage): '))
increase /= 100 # Convert number to decimal point

# Input validation
while increase < 0:
    print('Enter a non-negative number, try again.')
    organisms = int(input('Average daily increase (as a percentage): '))

# Input number of days left to multiply
days = int(input('\nNumber of days left to multiply: '))

# Input validation
while days < 0:
    print('Enter a non-negative number, try again.')
    days = int(input('Number of days left to multiply: '))

# Display header
print('\nDay Approximate\tPopulation')
for day in range(1, days + 1):
    if day == 1:
        print(f'{day:<16d}{day * organisms}')
    else:
        organisms = organisms + (organisms * increase)
        print(f'{day:<16d}{organisms:.3f}')
