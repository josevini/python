# Exercício 10.8 - Livro

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
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
        else:
            print('Saldo insuficiente!')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])
    def extrato(self):
        print('-' * 20)
        print(f'Extrato CC N° {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:5.2f}')
        print('-' * 20)

niara = Cliente('Vinicius', '9640-2432')
tony = Cliente('Niara', '8539-1321')
clientes = [niara, tony]

minhaConta = Conta(clientes, '2305', 500)
minhaConta.resumo()
