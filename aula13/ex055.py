maior = 0
menor = 0
for p in range(1, 6, 1):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print(f'\nO maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
