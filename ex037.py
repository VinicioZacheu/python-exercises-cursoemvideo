a1 = int(input('Chose your number:'))
print('In this Program, I will convert your chosen number in:')
print('Binary write (1)')
print('Octal write (2)')
print('Hexadecimal write (3)')
a2 = int(input('Write your conversion option:'))

if a2 == 1:
    print('{} in Binary mode is {}'.format(a1, bin(a1)[2:]))
elif a2 == 2:
    print('{} in Octal mode is {}'.format(a1, oct(a1)[2:]))
elif a2 == 3:
    print('{} in Hexadecimal mode is {}'.format(a1, hex(a1)[2:]))
else:
    print('Try a full number! Use option 1, 2 or 3')