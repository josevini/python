sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    NovoSal = sal + ((sal * 15) / 100)
else:
    NovoSal = sal + ((sal * 10) / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, NovoSal))
