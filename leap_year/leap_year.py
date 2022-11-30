# This program will tell you if a number you input is a leap year or not.
year = int(input("Which year do you want to check? "))

if year % 4 == 0 and ((year % 4) % 2 == 0):
    if year % 100 == 0 and ((year % 100) % 2 == 0):
        if year % 400 == 0 and ((year % 400) % 2 == 0):
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')