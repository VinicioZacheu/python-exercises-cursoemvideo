list = []
for c in range(0, 5):
    n = int(input('Write a value in the list: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('This number was added in the final of your list...')
    else:
        position = 0
        while position < len(list):
            if n <= list[position]:
                list.insert(position, n)
                print(f'This number was added in the position {position}*.')
                break
            position += 1
print(list)