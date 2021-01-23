from Clientes import Cliente
from Contas import Conta

vinicius = Cliente('Vinicius', '9640-2432')
print(f'Nome: {vinicius.nome} | Telefone: {vinicius.telefone}')

niara = Cliente('Niara', '8539-1321')
print(f'Nome: {niara.nome} | Telefone: {niara.telefone}')

minhaConta = Conta(vinicius, '2305', 600)
minhaConta.resumo()
