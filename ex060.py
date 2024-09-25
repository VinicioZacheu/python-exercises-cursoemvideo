from math import factorial
c = int(input('Write the number you want the factorial: '))
f = factorial(c)
print('{}'.format(c), end=' ')
for d in range(c-1, 0, -1):
    print('x {}'.format(d), end=' ')
print('= {}'.format(f))