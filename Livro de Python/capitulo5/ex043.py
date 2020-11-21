# Exercício 5.26 - Livro
dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))

div = dividendo
cont = 0
while True:
    div = div - divisor
    cont = cont + 1
    if div == 0:
        resultado = cont
        resto = 0
        break
    elif div < 0:
        resultado = cont - 1
        resto = div + divisor
        break
print(f'Resto da divisão: {resto}')
