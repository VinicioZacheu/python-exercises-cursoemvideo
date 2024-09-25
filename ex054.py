from datetime import date
date = date.today().year
adult = date - 18
for c in range(1,8):
    year = int(input('\033[mWrite de {}° person, year of born: '.format(c)))
    if year <= adult:
        print('\033[32mThis is an adult')
    else:
        print('\033[31mThis is not adult\n\033[36mHe will be adult in {}'.format(year+18))