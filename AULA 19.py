dictonery = {}
dictonery['movie'] = 'Star wars' #ADICIONAR
del dictonery['movi'] #DELETAR
dictonery.keys()
dictonery.values()
dictonery.items()
for k, v in dictonery.items():
    print(f'{k} = {v}')