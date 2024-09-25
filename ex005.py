# make a program that reads a number and displays its predecessor and successor

Number = int(input('Write a number!'))
predecessor = int(Number-1)
successor = int(Number+1)
print('The predecessor of {} is {}, The successor of {} is {}'.format(Number,predecessor,Number,successor))
