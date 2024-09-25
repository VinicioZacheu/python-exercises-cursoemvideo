print('This program will add how many number do you want, press 0 to stop! ')
amount = 0
c = 1
while c != 0:
    c = int(input('Number: '))
    amount = amount + c
print('The amount of this numbers add is {}'.format(amount))
