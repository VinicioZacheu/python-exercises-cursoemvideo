from time import sleep
print('''In this program we will find out, what is the classification of the triangle
The triangle can be equilateral: if 3 sides has the same size
The triangle can be isosceles: if 2 sides has the same size
The triangle can be scalene: if all sides has differents size''')
s1 = int(input('Write the first side of your triangle: '))
s2 = int(input('Write the second side of your triangle: '))
s3 = int(input('Write the third side of your triangle: '))
print('Analyzing sides...')
sleep(3)
if s1 + s2 >= s3 or s2 + s3 >= s1 or s3 + s1 >= s2:
    print('Congrats, This is a triangle ', end='')
    if s1 == s2 == s3:
        print('equilateral')
    elif s1 == s2 != s3 or s2 == s3 != s1 or s3 == s1 != s2:
        print('isosceles')
    elif s1 != s2 != s3 != s1:
        print('scalene')
else:
    print('Is not a triangle')



