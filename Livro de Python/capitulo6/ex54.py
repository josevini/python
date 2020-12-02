# Exercício 6.11 - Livro

numeros = [2, 6, 8, 4, 1, 20, -26]
menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num
print('=-=' * 10)
print(f'Menor → {menor}')
