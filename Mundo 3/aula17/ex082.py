lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    while 's' not in resp and 'n' not in resp:
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if 'n' in resp:
        break
print('-=' * 30)
lista_pares = []
lista_impares = []
for valor in lista:
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
