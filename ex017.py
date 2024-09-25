#Create a program that reads the opposite cathetus and the adjacent cathetus of a right triangle and shows the hypotenuse
import math
from math import sqrt
O = float(input('Write the length of opposite cathetus: '))
A = float(input('Write the length of adjacent cathetus: '))
H = (A**2 + O**2)
print('The Hypotenuse of a right triangle is {}'.format(math.sqrt(H)))