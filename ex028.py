#Write a game program that can randon think in a number, and his player have 1 chance to find the rigth number!
import random
from random import randint
from time import sleep
print('-=-'*20)
a = int(input('I will think in a number 0 to 5, and you need to guess the right number! \n Guess Your Number:  '))
print('-=-'*20)
b = randint(0, 5)
print('Processing...')
sleep(3)
if a == b:
    print('Your Answer is correct my number was {}'.format(b))
else:
    print('Your answer is rong my number was {}'.format(b))
print('-=-'*20)
