letra = input("Digite uma letra: ").lower()
if letra in 'aeiou':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")

    

texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")


print(range(10))

print(list(range(10)))