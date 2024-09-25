#write a program that can dimension the area of a wall and how many liters of paint you will need, to paint the wall, knowing that 1 liter can paint 2 square meters.
height = int(input('write the height of the wall :'))
width = int(input('write the width of the wall :'))
measure = height*width
paint = measure/2
print('The Dimension of your wall is: {}m2 and the amount of paint you will need is : {}L !'.format(measure,paint))