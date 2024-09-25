from random import randint
print('This is a MegaCena radiant game')
mega = []
games = []
a = int(input('How many games do you want? '))
cont2 = 1
while cont2 <= a:
    cont = 0
    while True:
        ran = randint(1, 60)
        if ran not in games:
            games.append(ran)
            cont += 1
        if cont >= 6:
            break
    games.sort()
    mega.append(games[:])
    games.clear()
    cont2 += 1
print('=-'*20)
for i, l in enumerate(mega):
    print(f'Games {i} = {l}')





