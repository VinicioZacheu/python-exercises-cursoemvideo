print('This program will show the average, the biggest value and de smallest value, you can stop whenever you want!')
average = 0
many = 0
biggest = 0
smallest = 0
Accept = False
while not Accept:
    numbers = int(input('Numbers: '))
    average = average + numbers
    many += 1
    if many == 1:
        biggest = smallest = numbers
    else:
        if numbers > biggest:
            biggest = numbers
        if numbers < smallest:
            smallest = numbers
    a = str(input('Do you wanna continue YES or NO? ')).upper().strip()[0]
    if a == 'N':
        Accept = True
print('The Average is {}, The biggest is {}, The smallest is {}.'.format(average/many, biggest, smallest))
