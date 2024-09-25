print('Gerador de PA')
print('-=-'*20)
first = int(input('What is the first term of your ARITHMETIC RATIO:  '))
ration = int(input('What is the ration for your ARITHMETIC RATIO: '))
a = first + ration*10
c = 1
b = first + ration*c
print('{} ->'.format(first), end=' ')
while b != a:
    print('{} ->'.format(first+ration*c), end=' ')
    c = c + 1
    b = first + ration * c
print('FIM')