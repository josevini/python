# Exercício 5.11 - Livro

dep = float(input('Informe o valor do depósito: '))
taxa = int(input('Taxa de juros: '))
mes = 1
saldo = dep
while mes <= 24:
    saldo += ((saldo * taxa) / 100)
    mes += 1
print(f'Total: {saldo - dep:.2f}')
