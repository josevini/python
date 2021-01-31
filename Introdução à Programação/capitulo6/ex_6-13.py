# Exercício 6.13 - Livro

t = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = menor = t[0]
soma = 0
for temp_atual in t:
    if menor > temp_atual:
        menor = temp_atual
    if maior < temp_atual:
        maior = temp_atual
    soma += temp_atual
media = soma / len(t)
print(f'Temperatura máxima: {maior}')
print(f'Temperatura mínima: {menor}')
print(f'Média de temperatura: {media}')
