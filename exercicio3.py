# Contagem de frequência
# Escreva uma função que recebe uma string e retorna um dicionário
# onde as chaves são os caracteres da string e os valores representam quantas vezes cada caractere aparece
# Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
# Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}


def contagem_frequencia(lista_strings):
    dicionario = {}
    for string in lista_strings:
        dicionario[string] = dicionario.get(string, 0) + 1
    return dicionario


linguagens_programacao = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']
print(contagem_frequencia(linguagens_programacao))