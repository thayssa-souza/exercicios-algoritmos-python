# Contagem de Palavras
# Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela
# Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências
# Exemplo: ["banana maçã banana laranja maçã maçã"]
# Saída: {"banana": 2, "maçã": 3, "laranja": 1}


def contagem_palavras(string):
    dicionario = {}
    string_separada = string.split(' ')
    for item in string_separada:
        dicionario[item] = dicionario.get(item, 0) + 1
    return dicionario


frutas = "banana maçã banana laranja maçã maçã"
print(contagem_palavras(frutas))