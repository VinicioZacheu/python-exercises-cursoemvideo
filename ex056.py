
avarage = 0
olddest = 0
nameold = 0
olddest = 0
age20f = 0
for p in range(1,5):
    name = str(input('{} {}* Person {}\nName: '.format('-'*5, p, '-'*5))).strip().upper()
    age = int(input('Age: '))
    sexo = str(input('Sex [M|F]: ')).strip().upper()
    avarage += age
    if p == 1 and sexo in 'Mm':
        olddest = age
        nameold = name
    if sexo in 'Mm' and age > olddest:
        olddest = age
        nameold = name
    if age < 20 and sexo in 'Ff':
        age20f += 1



print('In this group the age avarege is {:2f}.'.format(avarage/4))
print('Olddest man is {} and have {} years.'.format(nameold, olddest))
print('The amount of womans under 20 years old is {}. '.format(age20f))