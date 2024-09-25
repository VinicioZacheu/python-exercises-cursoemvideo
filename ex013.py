#Write a program that can show a increse of a salary of a worker by percentage!
Salary = float(input('write your salary: '))
increase = float(input('Write your increase salary percentage in real numbers: '))
applied = Salary*(increase+100)/100
print(applied)