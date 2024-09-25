print('This program will calculate your IMC')
high = float(input('Write your high (m) '))
weight = float(input('write yout weight (kg) '))
imc = weight/(high ** 2)
print('Your Imc is {:.2f}'.format(imc))
if imc >= 40:
    print('Morbid obesity, You need to lose weight!')
elif imc >=30 and imc < 40:
    print('You are obese')
elif imc <30 and imc >= 25:
    print('You are overweight')
elif imc <25 and imc >= 18.5:
    print('Your are in ideal weight')
else:
    print('Your are underweight, you need you gain weight ')
