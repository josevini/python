valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    while resp not in 's' and resp not in 'n':
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp in 'n':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')
