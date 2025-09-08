class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return self.cor    

        
class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass



class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# moto = Motocicleta("Vermelha", "ABC-1234", 2)
# moto.ligar_motor()
# carro = Carro("Azul", "XYZ-5678", 4)    
# carro.ligar_motor()
caminhao = Caminhao("Branco", "DEF-9012", 6, True)
print(caminhao.placa)
caminhao.ligar_motor()
print(caminhao)