print('-' * 35)
print('\t\tLOJAS SUPER BARATÃO')
print('-' * 35)
totalCompra = maisMil = menorPreco = c = 0
nomeMenor = ''
while True:
    nome = str(input('Nome do Produto: ')).capitalize()
    preco = float(input('Preço: R$'))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    c += 1
    totalCompra += preco
    if preco > 1000:
        maisMil += 1
    if c == 1:
        menorPreco = preco
        nomeMenor = nome
    else:
        if menorPreco > preco:
            menorPreco = preco
            nomeMenor = nome
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('----------- FIM DO PROGRAMA -----------')
print(f'O total da compra foi R${totalCompra:.2f}')
print(f'Temos {maisMil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {nomeMenor} que custa R${menorPreco:.2f}')
