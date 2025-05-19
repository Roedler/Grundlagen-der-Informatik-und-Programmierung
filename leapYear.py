year = int(input('Enter year: '))
leapYear = False
leapYearText = " not"

if year % 4 == 0:
    leapYear = True

if year % 100 == 0:
    leapYear = False

if year % 400 == 0:
    leapYear = True

if leapYear:
    leapYearText = ""

print(f'{year} is a{leapYearText} leap year!')