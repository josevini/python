class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
    def resumo(self):
        print(f'CC Número: {self.numero} Saldo: {self.saldo:.2f}')
    def saque(self, valor):
        if self.saldo >= valor:
            print('Fazendo saque!')
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')
    def deposito(self, valor):
        self.saldo += valor
        print('Fazendo depósito!')


