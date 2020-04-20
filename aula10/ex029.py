vel = int(input('Qual é a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
