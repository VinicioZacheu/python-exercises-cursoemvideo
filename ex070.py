print('This program will check total value, name, and cheapest')
total = cheapest = products = 0
while True:
    price = int(input('Product Price: '))
    name = str(input('Product name: '))
    cont = ''
    while cont not in 'YN':
      cont = str(input('Wanna Continue [Y/N]: ')).strip().upper()[0]
    total += price
    products += 1
    if products == 1:
        cheapest = price
    else:
        if price < cheapest:
            cheapest = price
    if cont == 'N':
        break
print(f'Your market list have {products}, the total value is {total}, and the cheapest products is {cheapest}')



