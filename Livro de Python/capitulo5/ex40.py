# Exercício 5.23 - Livro

n = int(input('Digite um número: '))
if n == 0 or n == 1:
    print(f'{n} é um caso especial')
else:
    cont = 1
    div = 0
    print(f'O valor {n} é divisível por ', end='')
    while cont <= 20:
        if n % cont == 0:
            print(cont, end=' ')
            div += 1
        cont += 1
    if div > 2:
        print(f' portanto, não é primo')
    else:
        print(f' portanto, é primo')
