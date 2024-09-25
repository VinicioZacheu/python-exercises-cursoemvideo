a = str(input('Write symbols, using parentheses correctly:'))
parentheses = []
for f in a:
    if f == '(':
        parentheses.append(f)
    elif f == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append('(')
if len(parentheses) > 0:
    print('Parentheses were used incorrectly')
else:
    print('Parentheses were use correctly:')





