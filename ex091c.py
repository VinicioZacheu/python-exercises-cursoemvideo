cor = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[0;30m'}

cores = ['padrao', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'branco']
def titulo(msg, color='padrao'):
    print(f'{cor[color]}{msg}{cor["padrao"]}', end='')

from random import randint

dicionary = dict()
d = e = 0
titulo('Dice Game', 'vermelho')
print()
titulo('How many players will play: ','roxo')
many = (int(input()))

for c in range(1,many+1):
    dicionary[f'Player {c}'] = randint(1,6)
for k,v in dicionary.items():
    d += 1
    titulo(f'{k} has dice played {v}', cores[d % len(cores)])
    print()
print('-='*20)
organize = dict(sorted(dicionary.items(), key=lambda item: item[1]))
for k, v in organize.items():
    d += 1
    titulo(f'The {d} place was: {k} ,he played {v} in the dice.', cores[d % len(cores)])
    print()
