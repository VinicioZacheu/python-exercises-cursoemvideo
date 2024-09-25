num = int(input('Write a number: '))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        primo += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if primo != 2:
    print('\n\033[35m Total of division this number accept is {},than he is not cousin '.format(primo))
else:
    print('\n\033[35m This number just accept 2 divisor, than he is a cousin number')