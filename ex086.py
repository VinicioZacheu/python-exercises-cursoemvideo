list = [[0,0,0],[0,0,0],[0,0,0]]
print(list)
for l in range (0,3):
    for c in range (0,3):
        list[l][c]= int(input(f'Input {l} {c}: '))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'| {list[l][c]:^5} |', end='')
    print()


