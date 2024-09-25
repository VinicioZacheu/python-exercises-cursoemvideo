dic = dict()
cont = average = media = 0
while True:
    dic['Name'] = str(input('Name: '))
    dic['sex'] = str(input('Sex W or M: ')).upper().strip()[0]
    dic['age'] = int(input('Age: '))
    c = str(input('Do you wanna continue Y|N: ')).upper().strip()[0]
    cont += 1
    average += dic['age']
    media = average / cont

    if c == 'N':
        break

for K, v in dic.items():
    if dic['age'] >= media:
        print(f'{dic.keys("name")}')
