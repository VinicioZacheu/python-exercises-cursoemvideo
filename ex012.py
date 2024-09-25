#Build a program that can read a product price and apply a percentual of discount.
product = float(input('Put your product price: '))
Discount = float(input('write you discount with real numbers: '))
applied = product*(100-Discount)/100
print('With the discount applied the new price of your product is {:.2f} Dolars'.format(applied))