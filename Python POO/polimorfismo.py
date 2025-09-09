class Passaro:
    def voar(self):
        print("Voando")

class Pardal(Passaro):
    pass

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ...")  


def plano_voo(obj):
    obj.voar()   



class Carro:
    def voar(self):
        print("Carro voador ativando propulsores!")    


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())    
plano_voo(Carro())           