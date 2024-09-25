v = int(input('Write the speed you drove in the freeway: '))
if v < 80:
    print('Nice you are a safe driver')
else:
    print('You are a bad drive, this is a ticket for you \r Your ticket is {}'.format((v-80)*7))
