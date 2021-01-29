# Exercício 5.18 - Livro
valor = int(input('Valor para saque: '))
ced = 0
ced_atual = 100
saque = valor
while True:
    if saque >= ced_atual:
        saque -= ced_atual
        ced += 1
    else:
        if ced != 0:
            print(f'{ced} cédulas de R${ced_atual}')
        if saque == 0:
            break
        if ced_atual == 100:
            ced_atual = 50
        elif ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 5
        elif ced_atual == 5:
            ced_atual = 1
        ced = 0
