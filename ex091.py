from random import randint
from operator import itemgetter
dict = {'Player 1': randint(1,6),
        'Player 2': randint(1,6),
        'Player 3': randint(1,6),
        'Player 4': randint(1,6)}
rank = []
for k, v in dict.items():
    print(f'{k} played : {v}')
rank = sorted(dict.items(), key=itemgetter(1), reverse=True)
print('-='*30)
for i,v in enumerate(rank):
    print(f'The {i+1}* place was {v[0]} if {v[1]} points.  ')