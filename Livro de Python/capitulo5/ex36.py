valor = int(input('Digite o valor a pagar: '))
ced = 0
ced_atual = 50
apagar = valor
while True:
    if ced_atual <= apagar:
        apagar -= ced_atual
        ced += 1
    else:
        if ced != 0:
            print(f'{ced} cédulas de R${ced_atual}')
        if apagar == 0:
            break
        if ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 5
        elif ced_atual == 5:
            ced_atual = 1
        ced = 0
