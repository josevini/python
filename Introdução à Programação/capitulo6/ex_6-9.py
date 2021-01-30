# Exercício 6.9 - Livro

lista = [2, 4, 5, 6]
p = int(input('Digite o valor p: '))
v = int(input('Digite o valor v: '))
achouP = achouV = False
pos_p = pos_v = 0
total_lista = len(lista)
pos = 0
while pos < total_lista:
    if lista[pos] == p:
        pos_p = pos
        achouP = True
    if lista[pos] == v:
        pos_v = pos
        achouV = True
    if achouP and achouV:
        break
    pos += 1
print('=-=' * 10)
if pos < total_lista:
    print(f'p: {p} foi encontrado')
    print(f'v: {v} foi encontrado')
    if pos_p < pos_v:
        print('p foi encontrado primeiro')
    elif pos_v < pos_p:
        print('v foi encontrado primeiro')
    else:
        print('Ambos foram encontrados na mesma posição')
else:
    if achouP:
        print(f'p: {p} foi encontrado')
    elif achouV:
        print(f'v: {v} foi encontrado')
    else:
        print('Nenhum valor foi encontrado!')
