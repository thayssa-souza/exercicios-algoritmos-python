# Ordenação de Tuplas
# Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
# escreva uma função que retorne a lista ordenada pela idade de forma crescente.


def ordenacao_idades(lista_tuplas):
    return sorted(lista_tuplas)


nome_idade = [("Samuel", 24), ("Karynne", 22), ("Carol", 21), ("Kleber", 23), ("Vinicius", 25)]
print(ordenacao_idades(nome_idade))