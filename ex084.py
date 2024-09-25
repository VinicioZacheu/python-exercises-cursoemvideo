list = []
people = []
lent = 0
maior = menor = 0
ph = ''
ps = ''
while True:
    name = str(input('Name: '))
    weigh = float(input('Kg:'))
    continu = str(input('Continue Y|N: ')).upper().strip()[0]
    people.append(name)
    people.append(weigh)
    list.append(people[:])
    if len(people) == 1:
        maior = menor = weigh
    else:
        if weigh > maior:
            maior = weigh
            ph = name
        if weigh < menor:
            menor = weigh
            ps = name
    people.clear()
    lent += 1
    if continu == 'N':
        break
print(f'{list}')
print(f'Number of members in this list {len(list)}, the tiniest person is {ps} with {menor}kg, the heavyset person is {ph} with {maior}kg')

