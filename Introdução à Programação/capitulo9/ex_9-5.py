# Exercício 9.5 - Livro

with open('pares.txt', 'r') as pares:
    valores_pares = pares.readlines()
    ultimo = len(valores_pares) - 1
    primeiro = -1
    for pos in range(ultimo, primeiro, -1):
        print(f'{valores_pares[pos]}', end='')
