
beginning = int(input('''In this game you will need to find how many dividers your number have.\nChose your number:  '''))
c = 1
d = 1
x = beginning/d
while x != 1:
    dividers = int(input('{}* divider: '.format(c)))
    d = d * dividers
    c += 1
    x = beginning / d
    print('{} |||| {}'.format(x, d))




print(d)