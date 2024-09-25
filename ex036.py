#Write that could check with you can aford a loans. The monthly installment need to be less than 30% of the salary!
a1 = int(input('What is the house price: '))
a2 = int(input('What is your salary: '))
a3 = int(input('How many years you would like to pay this house: '))
a4 = a1/(a3*12)
if a4 <= a2*0.3:
    print('Great Your loans was approved, your monthly installment is {}'.format(a4))
else:
    print('Unfortunately your loans was disapproved, try to pay in more years!')
