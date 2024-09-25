old = []
oldcopy = []
LList = []
DDict = dict()
register = 0
average = 0
Woman = 0
while True:
    DDict['Name'] = str(input('Write your name: ')).upper().strip()
    DDict['age'] = int(input('Age: '))
    while True:
        DDict['sex'] = str(input('W|M: ')).upper().strip()[0]
        if DDict['sex'] == 'WM':
            break
        print('Please write W or M')
    if DDict['sex'] == 'W':
        Woman += 1
    average += DDict['age']
    register += 1
    Raverage = average / register
    if DDict['age'] > Raverage:
        oldcopy.append(DDict['Name'])
        oldcopy.append(DDict['age'])
        oldcopy.append(DDict['sex'])
    old.append(oldcopy.copy())
    oldcopy.clear()
    LList.append(DDict.copy())
    while True:
        Continue = str(input('Wanna continue Y|N: ')).upper().strip()[0]
        if Continue == 'YN':
            break
        print('Please write a Y or N')
    if Continue == 'N':
        break
print('-='*20)
print(LList)
print(f'The amount of people registered is {register}')
print(f'The average age is {Raverage}')
print(f'People how has more than the average age {old}')
