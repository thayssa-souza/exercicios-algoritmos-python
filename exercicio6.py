# Combinação de dicionários
# Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são inteiros. 
# A função deve combinar os dicionários somando os valores das chaves que aparecem em ambos.
# Exemplo:
# d1 = {"a": 2, "b": 3, "c": 5}
# d2 = {"a": 1, "b": 4, "d": 7}
# Saída: {"a": 3, "b": 7, "c": 5, "d": 7}


def combinar_dicionarios(dicionario1, dicionario2):
    dicionario_soma = {}
    for chave in dicionario1.keys():
        if chave in dicionario2.keys():
            dicionario_soma[chave] = dicionario1[chave] + dicionario2[chave]
        else:
            dicionario_soma[chave] = dicionario1[chave]
    for chave in dicionario2.keys():
        if chave not in dicionario1.keys():
            dicionario_soma[chave] = dicionario2[chave]
    return dicionario_soma


d1 = {'a': 2, 'b': 3, 'c': 5}
d2 = {'a': 1, 'b': 4, 'd': 7}

print(combinar_dicionarios(d1, d2))
