print('This program will calculate your average in the last 3 tests! ')
t1 = int(input('Write your grade from the first test: '))
t2 = int(input('Write your grade from the second test: '))
t3 = int(input('Write your grade from the third test: '))
a = (t1 + t2 + t3)/3
print('Your avarage is {}'.format(a))
if a >= 7:
    print('Congratulation you have been approved')
elif a < 7 and a > 3:
    print('You are in summer school')
elif a <= 3:
    print('Unfortunately you have been reproved')