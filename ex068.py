from random import randint
print('Today we will play Even or Odd, choose your number between (1,10)! I will chose many!')
print('-=-'*20)
computer = randint(1,10)
many = 0
odd = 0
even = 0
win = 0
while True:
    player = int(input('Your Number: '))
    game = str(input('even/odd: ')).strip().upper()[0]
    winer = computer + player
    print(f'Your number {player}, Computer Number {computer}, sum {winer}!')
    if winer % 2 == 0:
        if game == 'E':
            win += 1
            print('You won')
        if game == 'O':
            break
    elif winer % 2 != 0:
        if game == 'E':
            break
        if game == 'O':
            win += 1
            print('You won')
    else:
        print('Character invalid try E/O')


print('-=-'*20)
print(f'You have won consecutively {win} times')