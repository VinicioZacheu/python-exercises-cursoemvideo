championchip = list()
player = dict()
while True:
    player['Name'] = str(input('Player Name: '))
    player['Games'] = int(input('How many games He Played?: '))
    for v in range(0, player["Games"]):
        player[f'Goals {v}'] = int(input(f'How many goals {player["Name"]} has made in the game {v+1}: '))
    championchip.append(player.copy())
    player.clear()
    while True:
        continu = str(input('Do you wanna continue Y|N: ')).strip().upper()[0]
        if continu in 'YN':
            break
    if continu == 'N':
        break
print('-='*30)
for k,v in enumerate(championchip):
    print(f'Para {k} temos {v}')
