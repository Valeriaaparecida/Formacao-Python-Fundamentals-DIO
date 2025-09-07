class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("Vermelha", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("Azul", "XYZ-5678", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "DEF-9012", 6)
caminhao.ligar_motor()