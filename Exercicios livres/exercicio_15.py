def contar_caracteres(string):
    contador = {}  # passo 1: dicionário vazio
    for caractere in string:  # passo 2: percorre cada caractere
        if caractere in contador:  # passo 3: já existe?
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador  # passo 4: retorna o resultado

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
