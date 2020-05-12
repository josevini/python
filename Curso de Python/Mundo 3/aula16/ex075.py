numeros = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

total = numeros.count(9)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {total} vez(es)')
if 3 in numeros:
    pos = numeros.index(3) + 1
    print(f'O valor 3 apareceu na {pos}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for valores in numeros:
    if valores % 2 == 0:
        print(valores, end=' ')
