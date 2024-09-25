from random import randint
numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'{numbers}')
print(f'The biggest value random was {max(numbers)}')
print(f'The smallest value random was {min(numbers)}')