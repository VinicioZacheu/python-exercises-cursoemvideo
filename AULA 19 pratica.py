clas = []
people1 = {'nome': 'gustavo', 'sex': 'M', 'age': 22}
people2 = {'nome': 'vinicio', 'sex': 'M', 'age': 21}
people1['Weight'] = str(input('Weight: '))
people2['Weight'] = str(input('Weight: '))
clas.append(people1.copy())
clas.append(people2.copy())
print(clas[1]['nome'])

