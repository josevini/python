dis = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(dis))
if dis <= 200:
    preço = dis * 0.50
    print('E o preço da sua passagem será R${:.2f}'.format(preço))
else:
    preço = dis * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
