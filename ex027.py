p = str(input('write the name of you business:')).strip()
d = p.split()
print('Analysing you business name:')
print('Your First business name is: {}'.format(d[0]))
print('Your last business name is: {}'.format(d[len(d)-1]))

