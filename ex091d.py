cor = {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[0;30m'}

cores = ['vermelho', 'verde', 'amarelo', 'roxo', 'azul']
def titulo(msg, color='padrao'):
    print(f'{cor[color]}{msg}{cor["padrao"]}', end='')

from random import randint
from time import sleep

dicionary = dict()

d = e = 0

print('-='*5)
titulo('DICE GAME', cores[3])

print()
print('-='*5)
sleep(1)

print()
print('-='*14)

titulo('How many players will play: ', cores[4])
many = (int(input()))

print('-='*14)
print()
print('-='*14)
for c in range(1, many+1):
    dicionary[f'Player {c}'] = {'dice': randint(1, 6), 'color': cores[(c-1)%len(cores)]}
    sleep(1)

for k, v in dicionary.items():
    titulo(f'{k} has dice played {v["dice"]}', v['color'])
    sleep(1)
    print()

print('-='*14)
print()

print('-='*26)

organize = dict(sorted(dicionary.items(), key=lambda item: item[1]['dice'], reverse=True))
for k, v in organize.items():
    d += 1
    titulo(f'The {d} place was: {k}, he played {v["dice"]} in the dice.', v['color'])
    sleep(1)
    print()

print('-='*26)