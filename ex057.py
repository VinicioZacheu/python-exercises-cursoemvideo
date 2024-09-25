sexo = str(input('Write your sex F|M: ')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Incorrect Sex, Write Your Sex [M|F]:')).strip().upper()[0]

print('sex register successfully {}'.format(sexo))


