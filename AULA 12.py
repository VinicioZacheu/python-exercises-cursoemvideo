#if
#elif
#else
# Estrutura condicional alinhada
Tax = int(input('How much Tax did you paid last month: '))
if Tax < 180000:
    print('You aliquot is 4%\n\033[31m the amount of Tax you should pay is R${}'.format(Tax*0.04))
elif Tax >= 180000 and Tax <= 360000:
    print('Your aliquot is 4% until 180.000 of invoicing, 7% after 180.000 of invoicing\n\033[31mThe amount of you should pay is {} '.format(180.000*0.04+(Tax-180.000)*0.07))
else:
    print('Your tax rate is 10% of your revenues above 360.000 plus 19.800, totalising \033[31m{}'.format(19.800+(Tax-360.000)*0.10))