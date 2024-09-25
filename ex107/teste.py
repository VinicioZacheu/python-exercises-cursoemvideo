from ex107 import moeda

while True:
    salary = float(input('What is your salary? '))
    way = str(input('Do you like to Add, subtract, dooble or halve: A|S|D|H ')).upper().strip()[0]
    if way == 'A':
        amount = float(input('The amount you want do add in %: '))
        print(f'Your new salary will be {moeda.aumento(salary, amount)}')
    elif way == 'S':
        amount = float(input('The amount you want to subtract in $: '))
        print(f'Your new salary will be {moeda.diminuir(salary, amount)}')
    elif way == 'D':
        print(f'Your new salary will be {moeda.dobrar(salary)}.')
    elif way == 'H':
        print(f'Yor new salary will be {moeda.metade(salary)}')
    continu = str(input('Do you wanna continue? Y|N: ')).upper().strip()[0]
    if continu == 'N':
        break



