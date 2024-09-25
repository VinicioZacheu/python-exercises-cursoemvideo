def leiaint(msg):
    global value
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            print(f'{n} is a int number, congratulation')
            break
        else:
            print(f'\033[0;31m{n} is not a int number, try again!\033[m')
    return value

n = leiaint('Write your number: ')
print(f'The return value was {n}, {value} ')
