from datetime import date
print('In this program we will found out, when was your military enlistment or when will be!')
y1 = int(input('What year were you born: '))
y2 = date.today().year
o3 = y2-y1
if o3 < 18:
    print('You will complete the age for military enlistment in {}'.format(y2+(18-o3)))
elif o3 == 18:
    print('This is your year of military enlistment!')
elif o3 > 18:
    print('You should military enlistment in {}'.format(y2-(o3-18)))