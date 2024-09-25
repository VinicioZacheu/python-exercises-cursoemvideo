from datetime import date
print('This program will find out What category you should Play')
y1 = int(input('What Year have you born?'))
y2 = date.today().year
age = y2-y1
print('Your athlete have {} years'.format(age))
if age <= 7:
    print('He is mirin class')
elif age <= 9:
    print('He is juvenil CLass')
elif age <= 11:
    print('He is adolecente class')
elif age <= 13:
    print('He is Junior class')
else:
    print('He is master Class')
