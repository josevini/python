from func import isBinary, toDecimal
sair = 'n'
print('=-=' * 10)
while True:
    num = str(input('Digite um valor na base 2: '))
    if isBinary(num):
        res = toDecimal(num)
        print(f'Decimal: {int(res)}')
    else:
        print('ERRO')
    res = str(input('Quer sair? [S/N] ')).lower()
    print('=-=' * 10)
    if res == 's':
        break
