
def vote(year):
    from datetime import date
    a = date.today().year
    age = a - year
    if age < 16:
        return f'You are to Young {age} years, your vote is illegal'
    elif age >= 18 and age <= 65:
        return f'You have {age} years, your vote is mandatory '
    elif age >= 16 and age < 18 or age > 65:
        return (f'You have {age} years, your vote is optional')


print(vote(int(input('What year have you born: '))))
