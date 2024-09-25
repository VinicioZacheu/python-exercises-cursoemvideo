list = []
while True:
    name = str(input('Name: '))
    test1 = int(input('first test: '))
    test2 = int(input('second test: '))
    continu = str(input('Do you wanna continue? Y|N: ')).strip().upper()[0]
    med = (test1+test2)/2
    list.append([name, [test1, test2], med])
    print(med)
    if continu == 'N':
        break
for i, a in enumerate(list):
    print(f'Student number: {i} | name: {a[0]} | Media : {a[2]} ')
while True:
    l = int(input('Do you Wanna all test? What Student?(Right 999 to Stop):  '))
    if l == 999:
        break
    if l <= len(list)-1:
        print(f'Student: {list[l][0]} | Grade: {list[l][1]}')