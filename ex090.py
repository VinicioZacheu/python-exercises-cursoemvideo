dict = {}

dict['name'] = str(input('Name: '))
dict['average'] = float(input(f'Average of {dict["name"]}: '))
if dict['average'] >= 7:
    dict['situation'] = 'Approved'
else:
    dict['situation'] = 'Reproved'
#print(f'Student: {dict["name"]}\nAverage: {dict["average"]}\nSituation: {dict["situation"]} ')
for k, v in dict.items():
    print(f'{k} is {v}')