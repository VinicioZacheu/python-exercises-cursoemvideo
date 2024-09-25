player = dict()
player['PLAYER'] = str(input('Player name: '))
games = int(input(f'How many games {player["PLAYER"]} has played? '))
for v in range(0,games):
    player[f'Game {v}'] = int(input(f'How many goals {player["PLAYER"]} has done in the game {v+1}: '))
print('-='*20)
for k, v in player.items():
    print(f'''For {k} we have {v} ''')
