print('Analysing deta')
num = (int(input('Write Value: ')), int(input('Write Value: ')), int(input('Write Value: ')), int(input('Write Value: ')))
print(f'9 appear {num.count(9)} times')
print(f'3 is in the position {num.index(3)+1}*')
even = 0
for n in num:
    if n % 2 == 0:
        even += 1
print(f'we have {even} even numbers')