list = [[], []]


while True:
    a = int(input('Write a number (0 to stop): '))
    if a % 2 == 0:
        list[0].append(a)
    if a % 2 == 1:
        list[1].append(a)
    if a == 0:
        break
list[0].sort()
list[1].sort()
print(list[0])
print(list[1])

