# Exercício 6.8 - Livro

lista = [2, 4, 5, 6]
total_lista = len(lista)
n = int(input('Digite o número a ser encontrado: '))
pos = 0
while pos < total_lista:
    if lista[pos] == n:
        break
    pos += 1
if pos < total_lista:
    print(f'Valor {n} encontrado na posição [{pos}]')
else:
    print('Número não encontrado!')
