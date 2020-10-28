# Exercício 5.7 - Livro

num = int(input('Número: '))
i = int(input('Início da tabuada: '))
f = int(input('Fim da tabuada: '))

while i <= f:
    print(f'{num} x {i} = {num * i}')
    i += 1
