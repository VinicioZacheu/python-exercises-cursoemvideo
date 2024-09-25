biggest = 0
smaller = 0
for w in range(1,6):
    kg = float(input(('Write the Weigth of {}* person: '.format(w))))
    if w == 1:
        biggest = kg
        smaller = kg
    else:
        if kg > biggest:
             biggest = kg
        if kg < smaller:
             smaller = kg

print('Smaller is {}'.format(smaller))
print('biggest is {}'.format(biggest))