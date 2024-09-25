print('Cash machining')
cash = int(input('What value do you want cash it out? '))
ced = 50
tced = 0
while True:
    if cash >= ced:
        cash -= ced
        tced += 1
    else:
        print(f'The amount of cedulas is {tced} of R${ced}')
        if cash >= 20:
            ced = 20
        elif cash >= 10:
            ced = 10
        elif cash >= 1:
            ced = 1
        tced = 0
        if cash == 0:
            break
