import datetime
from datetime import date
a = int(input('What year you would like to analysing \n If you wanna analysing this year Write 0 \n:'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('Your Year is leap year')
else:
    print('This Year is not leap Year:')