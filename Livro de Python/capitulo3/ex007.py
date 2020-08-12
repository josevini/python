# Exercício 3.11 - Livro
preco_mercadoria = float(input('Qual o preço da mercadoria? R$'))
desconto = int(input('Quanto será o desconto? '))
valor_desconto = ((preco_mercadoria * desconto) / 100)
novo_preco = preco_mercadoria - valor_desconto
print(f'O valor do produto antes era de R${preco_mercadoria}, com o desconto de {desconto}%, ele passa a custar R${novo_preco}')
