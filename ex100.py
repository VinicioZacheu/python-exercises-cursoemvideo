
from random import randint
from time import sleep
numeros = list()
def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')
def somapar(lista):
    soma = 0
    for value in lista:
        if value % 2 == 0:
            soma += value
    print(f'Adding the even values the total is {soma}')

sorteia(numeros)
somapar(numeros)
