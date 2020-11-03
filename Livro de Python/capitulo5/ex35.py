# Exercício 5.15 - Livro
total = 0
while True:
    preco = 0
    invalido = False
    cod = int(input('Código do produto (0 para sair): '))
    if cod == 0:
        print('=-=' * 10)
        break
    elif cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1
    elif cod == 3:
        preco = 4
    elif cod == 5:
        preco = 7
    elif cod == 9:
        preco = 8
    else:
        invalido = True
        print('Produto inválido!')
    if not invalido:
        qtd = int(input('Quantidade de vendas: '))
        total += (qtd * preco)
    print('=-=' * 10)

print(f'Total: R${total:.2f}')
