#   M - 20
#   MH + 18
#   H  ?
W = 0
MW = 0
M = 0
Continue = 'Y'
while Continue not in 'N':
    sex = str(input('What is your sex? ')).strip().upper()[0]
    age = int(input('What is your age? '))
    Continue = str(input('Do you wanna continue? N/Y: ')).strip().upper()[0]
    if age > 18:
        MW += 1
    if age > 20 and sex == 'WF':
        W += 1
    if sex == 'M':
        M += 1
    if Continue == 'N':
        break
print(f'Woman over 20 years: {W}\nPeople over 18 year {MW}\nMen: {M}')
