# Exercício 6.1 - Livro
notas = []
cont = soma = 0
while cont < 7:
    num = float(input(f'Nota {cont + 1}: '))
    notas.append(num)
    soma += notas[cont]
    cont += 1
media = soma / cont
print(f'{media:.2f}')
