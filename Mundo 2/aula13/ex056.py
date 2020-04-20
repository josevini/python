soma = 0
idade_velho = 0
nome_velho = ''
menos_20_anos = 0

for p in range(1, 5, 1):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'F' and idade < 20:
        menos_20_anos += 1
    if sexo == 'M' and idade_velho < idade:
        idade_velho = idade
        nome_velho = nome

media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}.')
print(f'Ao todo, são {menos_20_anos} mulheres com menos de 20 anos')
