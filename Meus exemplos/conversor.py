from func import *
sair = 'n'
print('---' * 10)
while True:
    num = getBinaryNumber('Digite um valor na base 2: ')
    res = toDecimal(num)
    print(f'Decimal: {int(res)}')
    res = str(input('Quer sair? [S/N] ')).lower()
    print('---' * 10)
    if res == 's':
        break
    elif res == 'n':
        continue
    else:
        print('Opção inválida!')
