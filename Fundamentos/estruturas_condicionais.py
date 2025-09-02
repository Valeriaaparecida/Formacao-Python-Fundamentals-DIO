idade = 15

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


nota = 75

if nota >= 90:
    print("Aprovado com excelência")
elif nota >= 60:
    print("Aprovado")
else:
    print("Reprovado")



idade = 20

mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)  


idade = 17
tem_autorizacao = True

if idade < 18:
    if tem_autorizacao:
        print("Pode entrar com autorização")
    else:
        print("Entrada negada")
else:
    print("Entrada liberada")




a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")
