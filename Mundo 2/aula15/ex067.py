while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 30)
    for mult in range(1, 11, 1):
        print(f'{num} x {mult} = {num * mult}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
