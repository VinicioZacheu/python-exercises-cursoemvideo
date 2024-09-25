print('This is a cash machining!')
cash = int(input('How much do you wanna take it out? '))
c50 = 50
c20 = 20
c10 = 10
c1 = 1
t50 = t20 = t10 = t1 = 0
while True:
    if cash >= c50:
        cash -= c50
        t50 += 1
    else:
        break
print(f'Total of Cedulas {t50} of R$50')
while True:
    if cash >= c20:
        cash -= 20
        t20 += 1
    else:
        break
print(f'Total of Cedulas {t20} of R$20')
while True:
    if cash >= c10:
        cash -= c10
        t10 += 1
    else:
        break
print(f'Total of cedulas {t10} of R$10')
while True:
    if cash >= c1:
        cash -= c1
        t1 += 1
    else:
        break
print(f'Total of cedulas {t1} of R$1')




