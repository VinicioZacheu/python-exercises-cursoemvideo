Start = int(input('Start from: '))
jump = int(input('Jump cases: '))
final = Start + (jump*10)
for c in range(Start,final,jump):
    print('{} -> '.format(c))

