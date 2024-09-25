from random import randint
Lista = ('Rock', 'Scissors', 'paper')
computador = randint(0, 2)
print('''Chose your option
Rock [0]
Scissors [1]
Papers [2]''')
jogador = int(input('What is your option? '))
print('you have chose {}, computer has chose {}'.format(Lista[jogador], Lista[computador]))
if computador == 0:
    if jogador == 0:
        print('Draw')
    elif jogador == 1:
        print('computer has won ')
    elif jogador == 2:
        print('Player has won')

elif computador == 1:
    if jogador == 0:
        print('Player won')
    elif jogador == 1:
        print('Draw')
    elif jogador == 2:
        print('Computer won')

elif computador == 2:
    if jogador == 0:
        print('Computer won')
    elif jogador == 1:
        print('player won')
    elif jogador == 2:
        print('Draw')


