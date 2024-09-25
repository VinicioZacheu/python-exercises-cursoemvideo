print('This program will sum numbers, until you wanna stop')
a = b = 0
while True:
    a = int(input('Write a number [Write 999 to stop}: '))
    if a == 999:
        break
    b += a
print(f'The sum of this numbers is {b}.')