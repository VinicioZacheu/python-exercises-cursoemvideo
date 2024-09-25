from time import sleep
print('This is a Number Analyser Program...')
first = int(input('First Number: '))
second = int(input('Second Number: '))
accept = False
while not accept:
    print('Processing...')
    sleep(1)
    print('-=-'*20)
    b = int(input('''[1] Sum\n[2] Multiply\n[3] Biggest\n[4] Another number\n[5] Finish process\nYour choice: '''))
    print('-=-'*20)
    if b == 1:
        print('{} + {} = {}'.format(first, second, first+second))
    elif b == 2:
        print('{} + {} = {}'.format(first, second, first*second))
    elif b == 3:
        if first > second:
            print('Between {} and {}, the biggest one is {}'.format(first, second, first))
        elif second > first:
            print('Between {} and {}, the biggest one is {}'.format(first, second, second))
        elif second == first:
            print('Both have the same value, they are equal')
    elif b == 4:
        first = int(input('Write the first number: '))
        second = int(input('Write the second number: '))
    elif b == 5:
        accept = True