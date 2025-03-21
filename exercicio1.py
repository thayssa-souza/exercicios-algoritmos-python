# Soma de elementos pares
# Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os elementos pares contidos nela.
# Exemplo: [2,4,10,3,9,7,15,22]
# Saída: A soma dos pares é: x

def soma_numeros_pares(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma += numero
    return soma


lista_inteiros = [2, 4, 10, 3, 9, 7, 15, 22]
soma_total = soma_numeros_pares(lista_inteiros)
print(f'A soma dos pares é: {soma_total}')