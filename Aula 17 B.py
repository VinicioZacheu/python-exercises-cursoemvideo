value = []
value.append(5)
value.append(3)
value.append(4)
for cont in range(0, 5):
    value.append(int(input('Write Your Value: ')))

for c, v in enumerate(value):
    print(f'In postion {c} I founded the value {v}')
