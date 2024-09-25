#duplas [] imutavel
#listas [] mutavel
#.list []
#.appendp[''] finalGFV
#.insert[0,''] add in the place other members in this list go up
#del lanche[3]
#pop[por item] - ,pop[] vai remover o ultimo elemento
#remove['conteudo']
#valores = list(range(4,11))

# organizar valores em ordem
#.sort()
#.sort(reverse=True)

#len(list) tamanho
num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
num.pop(1)
num
print(num)
print(f'Essa lista tem {len(num)}')