class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # atributo protegido

    # Getter para saldo
    @property
    def saldo(self):
        return self._saldo

    # Setter para saldo (não deixa saldo ser negativo direto)
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print(" Saldo não pode ser negativo!")

    # Método para depósito
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f" Depósito de R$ {valor} realizado com sucesso!")
        else:
            print(" Valor inválido para depósito.")

    # Método para saque
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f" Saque de R$ {valor} realizado com sucesso!")
        else:
            print(" Saque inválido ou saldo insuficiente.")

conta = ContaBancaria("Gis", 1000)

print(conta.saldo)     
conta.depositar(500)   
print(conta.saldo)     

conta.sacar(300)       
print(conta.saldo)    

conta.saldo = -200    
print(conta.saldo)     

conta.saldo = -200     
print(conta.saldo)      
