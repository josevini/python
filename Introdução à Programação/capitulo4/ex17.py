# Exercício 4.6 - Livro

dis = float(input('Distância da viagem: '))
preco = 0
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print(f'Valor a se pagar: R${preco}')
