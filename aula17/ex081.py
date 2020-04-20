valores = []

while True:
    v = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    valores.append(v)
    while 's' not in resp and 'n' not in resp:
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp in 'n':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
print('O valor 5 ', end='')
if 5 in valores:
    pos = (valores.index(5)) + 1
    print(f'é o {pos}ª valor da lista!')
else:
    print('não se encontra na lista!')
