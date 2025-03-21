# Tupla de médias
# Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas notas, 
# crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do aluno e sua média de notas.
# Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
# Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

def tupla_medias(dicionario_notas):
    lista_medias = []
    for chave, valor in dicionario_notas.items():
        media_notas = sum(valor)/len(valor)
        media_arredondada = round(media_notas, 2)
        lista_medias.append((chave, media_arredondada))
    return lista_medias


dicionario_notas = {'Ana': [8, 9, 7], 'Bruno': [5, 6, 5], 'Carlos': [10, 9, 10]}
print(tupla_medias(dicionario_notas))