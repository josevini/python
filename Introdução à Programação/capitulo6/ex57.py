# Exercício 6.17 - Livro

estoque = {
    'tomate': [50, 2.30],
    'alface': [35, 0.45],
    'batata': [60, 1.20],
    'feijão': [20, 1.50]
}
while True:
    print('=-=' * 10)
    produto = str(input('Informe o produto desejado: ')).lower()
    if produto == 'sair':
        print('FIM')
        break
    elif produto not in estoque.keys():
        print('Produto não cadastrado!')
    else:
        quantidade = int(input('Informe a quantidade a comprar: '))
        if estoque[produto][0] < quantidade:
            print('Não há essa quantidade estocada!')
        else:
            estoque[produto][0] -= quantidade
            preco = estoque[produto][1]
            total = preco * quantidade
            print(f'{produto.capitalize()}: R${preco:.2f} x {quantidade} = R${total:.2f}')

print('=-=' * 10)
print(f"{'PRODUTOS'}{'QUANTIDADES':^15}{'PREÇOS'}")
for chave, valor in estoque.items():
    qtd = valor[0]
    preco = valor[1]
    if qtd == 0:
        print(f'{chave.capitalize()} {"ACABOU":^16} {preco:>3.2f}')
    else:
        print(f'{chave.capitalize()} {qtd:>9} {preco:>11.2f}')
