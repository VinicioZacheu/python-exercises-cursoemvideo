import random
from random import choice

n1 = str(input('Write the name of the first student: '))
n2 = str(input('Write the name of the second student: '))
n3 = str(input('write the name of the third student: '))
n4 = str(input('write the name of the fourth student: '))
lista = [n1,n2,n3,n4]
print('the chosen one is: {}.'.format(random.choice(lista)))

