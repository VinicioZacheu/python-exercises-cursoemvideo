#Write a program that can check with 3 lines can make a triangle
a = int(input('Write the fist line: '))
b = int(input('Write the second line: '))
c = int(input('Write the third line: '))
if a + b > c and a + c > b and c + b > a:
    print('This lines can build a triangle!')
else:
    print('Unfortunately your lines can not be a triangle!')