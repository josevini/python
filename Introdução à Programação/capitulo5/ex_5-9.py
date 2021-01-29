# Exercício 5.9 - Livro

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0
cont = dividendo
while cont >= divisor:
    cont -= divisor
    quociente += 1
resto = cont
print(f'Resultado: {quociente}')
print(f'Resto: {resto}')
