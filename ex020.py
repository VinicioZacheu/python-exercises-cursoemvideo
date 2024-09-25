import random
from random import shuffle

n1 = str(input("Write the name of your first student: "))
n2 = str(input('Write the name of your second student: '))
n3 = str(input('write the name of your third student: '))
n4 = str(input('write the name of your fourth student: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('The order of student will do the presentation is {}'.format(lista))
