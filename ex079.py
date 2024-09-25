list = []
while True:
    n = int(input('Write a number for your list (Write 999 to stop):'))
    if n in list:
        print('Duplicate value, try again...')
    if n not in list and n != 999:
        list.append(n)
        print('Value added successful')
    if n == 999:
        break
list.sort()
print(list)