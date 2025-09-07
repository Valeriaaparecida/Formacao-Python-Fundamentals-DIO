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


b1 = Bicicleta("Caloi", "Mountain Bike", 2021, "Vermelha", 1500.00)
b1.buzinar()
b1.correr()
b1.parar()