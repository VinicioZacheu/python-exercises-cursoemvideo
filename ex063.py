print('This program will create a fibonatti sequence! ')
print('-=-'*20)
lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
terms = int(input('How many terms you want show: '))
t1 = 0
t2 = 1
print('{} -> {} ->'.format(t1, t2), end=' ')
c = 3
add = 1
while add > 0:
    terms = terms + add
    while c <= terms:
        t3 = t1 + t2
        print('{} ->'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        c += 1
    print('S2')
    add = int(input('\nDo you wanna add more terms? How many? '))
print('Total of terms is {}'.format(terms))
print('END')



