from  time import sleep
def biggest(* num):
    cont = big = 0
    print('\nAnalysing the values:  ')
    for value in num:
        print(f'{value}',end= ' ' )
        sleep(0.3)
        if cont == 0:
             big = value
        else:
            if value > big:
                big = value
        cont += 1
    print('')
    print('-=' * 20)
    print(f'was informed {cont} values.')
    print(f'The biggest value informed was {big}.')


biggest(2, 9, 4, 5, 7, 1)
biggest(4, 7, 0)
biggest(1, 2)
biggest(6)
biggest()
