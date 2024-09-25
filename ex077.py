print('Analysing ')
sentence =('cachorro', 'gato', 'cobra', 'elefante', 'paralelepipedo')
for words in sentence:
    print(f'{words} =', end= ' ')
    for character in words:
        if character.lower() in 'aeiou':
            print(character, end= ' | ')