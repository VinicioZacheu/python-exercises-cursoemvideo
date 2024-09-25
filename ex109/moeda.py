def aumento(valor=0, indice=0, formato=0):
    res = valor + (valor * indice/100)
    return res


def diminuir(valor=0, indice=0, formato=0):
    res = valor - (valor * indice/100)
    return res


def dobrar(valor, indice=0, formato=0):
    res = valor * 2
    return res


def metade(valor=0, formato=False):
    res = valor / 2
    return res

def moeda(valor=0, moeda='R$', formato=False):
    return f'{moeda}{valor:>.2f}'.replace(',','.')