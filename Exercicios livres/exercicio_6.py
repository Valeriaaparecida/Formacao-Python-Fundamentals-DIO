num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % num2 == 0 :
    print(f"{num1} é múltiplo de {num2}")
elif num2 % num1 == 0 :
    print(f"{num2} é múltiplo de {num1}")
else:
    print("Nenhum dos números é múltiplo do outro.")