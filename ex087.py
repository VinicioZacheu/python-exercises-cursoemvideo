list = [[0,0,0],[0,0,0],[0,0,0]]
par = []
pares = 0
soma = 0
biggest = 0
print(list)
B2 = 0
for l in range (0,3):
    for c in range (0,3):
        list[l][c]= int(input(f'Input in position [{l}] [{c}]: '))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'| {list[l][c]:^5} |', end='')
        if list[l][c] % 2 == 0:
            par.append(list[l][c])
            pares += list[l][c]
    print()
for s in range(0, 3):
    soma += list[s][2]
    print()
for b in range(0, 3):
    if b == 0:
        biggest = b
    elif list[1][b] > biggest:
        biggest = list[1][b]
print('-='*30)
print(f'The biggest Value in the second line is {biggest}')
print(f'addition in par number {pares}\n{par}')
print(f'addition in third column = {list[0][2] + list[1][2] + list[2][2]}')
print(f'addition in column other way = {soma}')






