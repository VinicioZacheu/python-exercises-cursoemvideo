# Create an algorthm, that reads a number and shows its double triple and root.
Number = int(input('Write a number: '))
Double = Number*2
Triple = Number*3
Root = Number**(1/2)
print('The Number is {} \nHis double is {} \nHis triple is {} \nHis root is {:.2f}.'.format(Number,Double,Triple,Root))