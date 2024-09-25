list = ('peperoni', 49.90,
    'calabresa', 39.90,
    'mafiosa', 45.90,
    'portuguesa', 42.00,
    'Margherita', 45.90,
    'Amalfi', 43.90,
    'napoli', 45.90,
    'caprese', 44.80)
print('-'*40)
print('Pizza Menu')
print('-'*40)
for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<30}', end='')
    else:
        print(f'R${list[item]:>6.2f}')
