list = []
t = 0
while True:
    n = int(input('Write the number do you wanna add in your list: '))
    list.append(n)
    stop = str(input('Do you wanna continue? N to Stop Y continue: ')).strip().upper()[0]
    t += 1
    while stop not in 'YN':
        stop = str(input('Do you wanna continue? N to Stop, yes to continue: ')).strip().upper()[0]
    if stop == "N":
        break
list.sort(reverse=True)
print(list)
print(f'Itens in this list {t}')
if 5 in list:
    print('5 is on the list')
else:
    print('5 is not on list')



