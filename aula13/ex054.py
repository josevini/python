from datetime import date
atual = date.today()
menor = 0
maior = 0
for c in range(1, 8, 1):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if (atual.year - nasc) < 18:
        menor += 1
    else:
        maior += 1

print(f'\nAo todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
