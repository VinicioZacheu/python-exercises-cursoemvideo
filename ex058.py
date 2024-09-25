import random
from time import sleep
from random import randint
print('Lets Play a game, I will think in one number from 0 to 100, you will need to discover this number...')
computer = randint(0,100)
print("{}-".format("-")*40)
c = 1
guess = int(input('Guess your number, {}* time: '.format(c)))
while guess != computer:
    c += 1
    if computer > guess:
        guess = int(input('You are wrong try higher numbers, {}* time: '.format(c)))
    elif computer < guess:
        guess = int(input('To higher try lower numbers {}* time: '.format(c)))

print("Congratulation you hit the computer number in {}* times.".format(c))
