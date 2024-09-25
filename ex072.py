print('Chose a number and receive the same number ')
numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
while True:
    num = int(input('What number do you wanna see [0-20]: '))
    if 20 >= num >= 1:
        break
print(numbers[num-1])

