import math
from math import sin, cos, tan, radians
A = float(input("Write your Angle: "))
print('Angle {} have a sine as {:.2f}\n a cosine as {:.2f}\n a hypotenuse as {:.2f}'.format(A, math.sin(math.radians(A)), math.cos(math.radians(A)), math.tan(math.radians(A))))
