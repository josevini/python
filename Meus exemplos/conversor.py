from func import *
print('---' * 10)
while True:
    num = getBinaryNumber('Digite um valor na base 2: ')
    resp = toDecimal(num)
    print(f'Decimal: {int(resp)}')
    resp = question('Quer sair? [S/N] ')
    print('---' * 10)
    if resp:
        break
    else:
        continue
