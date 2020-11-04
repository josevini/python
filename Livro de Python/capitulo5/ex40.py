# Exercício 5.23 - Livro

n = int(input('Digite um número: '))
if n == 0 or n == 1:
    print(f'{n} é um caso especial')
else:
    cont = 1
    div = 0
    while cont <= 5:
        if n % cont == 0:
            div += 1
        cont += 1
    if div > 2:
        print(f'{n} não é primo')
    else:
        print(f'{n} é primo')
