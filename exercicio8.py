# Verificador de Palíndromos
# Escreva uma função que recebe uma palavra e retorna True se for um palíndromo e False caso contrário.
# Exemplo:
# entrada = "radar"
# Saída: True


def verificador_palindromos(palavra):
    tamanho_palavra = len(palavra)
    metade_palavra = tamanho_palavra % 2
    if metade_palavra == 0:
        metade_palavra = tamanho_palavra / 2
    else:
        metade_palavra = (tamanho_palavra - 1) / 2

    for i in range(int(metade_palavra)):
        if palavra[i] != palavra[tamanho_palavra - i - 1]:
            return False
        else:
            return True


print(verificador_palindromos('radar'))
print(verificador_palindromos('baleia'))
print(verificador_palindromos('arara'))