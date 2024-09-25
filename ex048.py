count = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        soma = soma + c
print('The amount of numbers divisible for 3 and odd, from 1 to 500 is {}. Add up all of than we have {} '.format(count, soma))



