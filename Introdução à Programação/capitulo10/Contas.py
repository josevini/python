class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('--' * 16)
        print(f'Dono(s) da conta: ', end='')
        try:
            for cliente in self.clientes:
                print(cliente.nome, end=' ')
            print('')
        except TypeError:
            print(self.clientes.nome)
        print(f'CC Número: {self.numero} Saldo: {self.saldo:.2f}')
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        else:
            return False
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])
    def extrato(self):
        print('-' * 20)
        print(f'Extrato CC N° {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:5.2f}')
        print('-' * 20)

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        else:
            return False
