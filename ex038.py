print('In this challenge we will find the upper number! ')
n1 = int(input('Write you first number:'))
n2 = int(input('Write Your second number:'))
if n1 > n2:
    print('{} is bigger than {}'.format(n1, n2))
elif n1 < n2:
    print('{} is bigger than {}'.format(n2, n1))
else:
    print('They are the same')