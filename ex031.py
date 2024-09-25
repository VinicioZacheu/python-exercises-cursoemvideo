Km = int(input('How much Km your travel have: '))
P = Km/2
P2 = 100 + (Km-200)/3
if Km < 200:
    print('Your ticket price is {}'.format(P))
else:
    print('Your ticket price is: {}'.format(P2))