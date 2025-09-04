SECRETO = 1234
senha = int(input("Digite a senha: "))
if senha == SECRETO:
    print("Acesso permitido.")
else:
    print("Acesso negado.")