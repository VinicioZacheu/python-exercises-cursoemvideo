print('This program will build a Arithmetic Ratio ')
first = int(input('First Term of your Arithmetical ratio: '))
ratio = int(input('Ratio: '))
terms = int(input('How many terms do you want: '))
w = 0
add = 1
while add > 0:
    terms += add
    while w != terms:
        print('{} ->'.format(first + ratio * w), end=' ')
        w = w + 1
    print('Pause')
    add = int(input('How many terms you would like to add?: '))
print('END')
