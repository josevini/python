qtd = int(input('Quantos números primos você deseja ver? '))

num = 1
cont = 1
print(f'Os {qtd} primeiros números primos são ', end='')
while cont <= qtd:
    inicio = 1
    fim = num
    div = 0
    while inicio <= fim:
        if num % inicio == 0:
            div += 1
        inicio += 1
    if div == 2:
        print(f'{num}', end=', ' if cont <= (qtd - 1) else '.')
        cont += 1
    num += 1
