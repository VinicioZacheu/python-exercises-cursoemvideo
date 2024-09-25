from random import randint

dicionary = dict()
d = 0
print('\033[0;31;40mDice Game\033[m')
many = int(input('How many players will play: '))
for c in range(1,many+1):
    dicionary[f'Player {c}'] = randint(1,6)
for k,v in dicionary.items():
    print(f'{k} has dice played {v}')
print('-='*20)
organize = dict(sorted(dicionary.items(), key=lambda item: item[1]))
for k, v in organize.items():
    d += 1
    print(f'The {d} place was, {k} ,he player {v} in the dice')

