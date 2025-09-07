class Bicicleta:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco

    def buzinar(self):
        print("Plim plim...")
       

    def parar(self):
        print("Parando bicileta...")
        print("Bicicleta parada!")

    def correr(self):
            print("Vrummmm...")

    def __str__(self):
         return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.preco}"
    def __str__(self):
         return f"{self.__class__.__name__} : {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"

# b1 = Bicicleta("Caloi", "Mountain Bike", 2021, "Vermelha", 1500.00)
# b1.buzinar()
# b1.correr()
# b1.parar()

b2 = Bicicleta("Monark", "Speed", 2020, "Azul", 1200)
print(b2)