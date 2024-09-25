list = []
l2 = []
l1 = []
stop = 'y'
while stop not in 'N':
    n = int(input('Number to add: '))
    list.append(n)
    stop = str(input('Continue Y|N: ')).upper().strip()[0]
    while stop not in 'YN':
        stop = str(input('Continue N|Y:: ')).upper().strip()[0]
    if n % 2 == 0:
        l2.append(n)
    if n % 2 == 1:
        l1.append(n)
print(f'All the number {list}')
print(f'Odd numbers {l1}')
print(f'Even numbers {l2}')