soma = 0
for c in range(1,7):
    value = int(input('Write a value:'))
    if value % 2 == 0:
        soma = soma + value
print('A soma dos valores pares e {}'.format(soma))


