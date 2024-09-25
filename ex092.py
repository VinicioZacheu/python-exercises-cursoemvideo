from datetime import datetime
Dict = dict()
Dict['name'] = str(input('Name: '))
birth = int(input('Day of birth: '))
Dict['Work Wallet'] = int(input('Work Wallet [0 to none]: '))
Dict['age'] = datetime.now().year - birth
if Dict['Work Wallet'] != 0:
    Dict['Start Work'] = int(input('Year you start to work: '))
    Dict['Salary'] = int(input('How much you get paid: '))
    Dict['Retired Year'] = Dict['Start Work'] + 35
    Dict['Retired Age'] = Dict['Retired Year'] - birth

for k, v in Dict.items():
    print(f'For {k} We Have {v}')

