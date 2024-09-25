def cont(b,f,s):
    if s == 0:
        s = 1
    if s < 0:
        s *= -1
    print(f'This program will cont {b} to {f} with spacing of {s}')
    if b < f:
        for a in range(b, f+1):
             if a % s == 0:
                print(a)

    else:
        con = b
        while con >= f:
            print(f'{con}')
            con -= s


b = int(input('Cont Beginning: '))
f = int(input('Cont Final: '))
s = int(input('Cont Space: '))
cont(b, f, s)
