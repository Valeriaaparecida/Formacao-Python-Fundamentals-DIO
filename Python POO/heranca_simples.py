class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}(cor={self.cor}, placa={self.placa}, numero_rodas={self.numero_rodas})"    

class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def  __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print("O caminhão está carregado" if self.carregado else "O caminhão não está carregado")
      
    def __str__(self):
        return f"{self.__class__.__name__}(cor={self.cor}, placa={self.placa}, numero_rodas={self.numero_rodas}, carregado={self.carregado})"  
moto = Motocicleta("Vermelha", "ABC-1234", 2)
carro = Carro("Azul", "XYZ-5678", 4)
caminhao = Caminhao("Branco", "DEF-9012", 6, True)


print(moto)
print(carro)
print(caminhao)