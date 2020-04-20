valores = []
maior = menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {pos}: ')))
    if pos == 0:
        maior = valores[pos]
        menor = valores[pos]
    else:
        if maior < valores[pos]:
            maior = valores[pos]
        if menor > valores[pos]:
            menor = valores[pos]
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, val in enumerate(valores):
    if maior == val:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos in range(0, len(valores)):
    if menor == valores[pos]:
        print(f'{pos}...', end=' ')
