a = int(input('Write your first number: '))
b = int(input('Write your second number: '))
c = int(input('Write you Third number: '))
if a < b < c:
    smallest = a
    half = b
    biggest = c
if b < c < a:
    smallest = b
    half = c
    biggest = a
if c < a < b:
    smallest = c
    half = a
    biggest = b
if a < c < b:
    smallest = a
    half = c
    biggest = b
if c < b < a:
    smallest = c
    half = b
    biggest = a
if b < a < c:
    smallest = b
    half = a
    biggest = c
print('The Biggest value is {} the second value is {} the smallest valeu is {}'.format(biggest, half, smallest ))
