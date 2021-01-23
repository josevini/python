from Clientes import Cliente
from Contas import Conta

vinicius = Cliente('Vinicius', '9640-2432')
niara = Cliente('Niara', '8539-1321')
clientes = [vinicius, niara]

minhaConta = Conta(vinicius, '2305', 600)
nossaConta = Conta(clientes, '0709', 1200)

minhaConta.deposito(6400)
minhaConta.saque(2000)

minhaConta.extrato()
