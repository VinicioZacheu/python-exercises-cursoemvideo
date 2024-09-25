from time import sleep
print('This program will show the TABUADA of any number, until you ask to stop')
a = 1
while True:
    number = int(input('Number: '))
    if number < 0:
        break
    while a <= 10:
        sleep(1)
        print(f'{a} x {number} = {a * number}')
        a += 1



