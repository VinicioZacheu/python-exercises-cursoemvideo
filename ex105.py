from time import sleep
def nota(*n, sit=False):
    r = dict()
    r['Maior Nota'] = max(n)
    r['Samallest Grade'] = min(n)
    r['Total Grades'] = len(n)
    r['Average Grade'] = sum(n)/len(n)
    if sit:
        if r['Average Grade'] >= 8:
            r['Grade Situation'] = 'Good'
        elif r['Average Grade'] > 6:
            r['Grade Situation'] = 'Regular'
        else:
            r['Grade Situation'] = 'Bad'
    return r


sleep(2)

test = list()
g = int(input('How many test have you done?: '))
for c in range(1, g+1):
    tes = float(input(f'Your Grade {c}* test: '))
    test.append(tes)

nota(test, sit=True)



