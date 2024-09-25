name = str(input('Write a sentence: ')).strip().upper()
words = name.split()
together = ''.join(words)
reverse = ''
for letter in range(len(together) -1, -1,-1):
    reverse = reverse + together[letter]
print('The reverse of {} is {}'.format(together, reverse))
if reverse == together:
    print('This sentence is a palindrome')
else:
    print('This sentence is not a palindrome')