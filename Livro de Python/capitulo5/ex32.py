# Exercício 5.12 - Livro

dep = float(input('Informe o valor do depósito: '))
taxa = int(input('Taxa de juros: '))
invest = float(input('Valor mensal: '))
mes = 1
saldo = dep
while mes <= 24:
    saldo += ((saldo * taxa) / 100) + invest
    mes += 1
print(f'Total: {saldo - dep:.2f}')
