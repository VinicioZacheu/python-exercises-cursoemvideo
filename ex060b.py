a = int(input('Write the factorial you would like to know: '))
b = a
d = 1
print('{}! ='.format(a),end=' ')
while b != 0:
    print('{}'.format(b),end=' ')
    print('x'if b > 1 else '=', end=' ')
    d *= b
    b -= 1
print(d)
