pre = float(input('Qual é o preço do produto? R$'))
des = (pre * 5) / 100
Npre = pre - des
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pre, Npre))
