from func import *
sair = 'n'

while True:
    num = getBinaryNumber('Digite um valor na base 2: ')
    if isBinary(num):
        res = toDecimal(num)
        print(f'Decimal: {int(res)}')
    else:
        print('ERRO')
    res = str(input('Quer sair? [S/N] ')).lower()
    print('=-=' * 10)
    if res == 's':
        break
    elif res == 'n':
        continue
    else:
        print('Opção inválida!')
