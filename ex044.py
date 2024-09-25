from time import sleep
print('This program will calculate the amount You will pay for 1 pizza and all methods you can use to pay!')
Pizza = float(input('How much does this pizza cost: '))
methods = float(input('''How would you like to pay this pizza?
[1] cash/check 10% discount
[2] cash on the card 5% discount
[3] in up 2 installments on the card 
[4] 3x or more on the card 20% interest 
Chose your payment method: '''))
if methods == 1:
    print('The amount is {}'.format(Pizza*0.90))
elif methods == 2:
    print('The amount is {}'.format(Pizza*0.95))
elif methods == 3:
    print('The amount is {}, 2 installments of {}'.format(Pizza, Pizza/2))
elif methods == 4:
    print('The amount you will pay is {}'.format(Pizza*1.20))
    installments = int(input('How many installments would you like? '))
    a = (Pizza*1.20)/installments
    print('Processing...')
    sleep(2)
    print('You will pay {} installment of R${}'.format(installments, a))



