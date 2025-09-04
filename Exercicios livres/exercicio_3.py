idade = int(input("Digite sua idade: "))
if idade >= 18 and idade < 65:
    print("Você é maior de idade e pode votar.")
elif idade <= 17:
    print("Você é menor de idade e não pode votar.")
else:
    print("Votar é opcional para você.")