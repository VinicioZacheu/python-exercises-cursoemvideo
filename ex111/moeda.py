def aumento(valor=0, indice=0, formato=False):
    res = valor + (valor * indice/100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, indice=0, formato=False):
    res = valor - (valor * indice/100)
    return res if formato is False else moeda(res)


def dobrar(valor, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace(',','.')


def resumo(valor=0, aument=5, diminui=10):
     print(f'''Your increase salary is {aument}% tota is {aumento(valor,aument,True)}\nYour deduction salary is {diminui}, total: {diminuir(valor,diminui,True)}\nDoble is {dobrar(valor,True)}\n Half is {metade(valor,True)} ''')


