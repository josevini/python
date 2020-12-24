# Exercício 5.13 - Livro

divida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mes = 1
if (divida * (taxa / 100) > pagamento):
    print("Sua divida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print("Saldo da divida no mês %d é de R$%6.2f." % (mes, saldo))
        mes = mes + 1
    print(f'Para pagar uma divida de R${divida:.2f}, a {taxa} de juros, ')
    print(f'você precisará de {mes - 1} meses, pagando um total de R${juros_pago:.2f} de juros.')
    print(f'No último mês, você teria um saldo residual de R${saldo:.2f} a pagar.')
