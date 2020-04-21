count = maior = menor = 0
pessoas = list()
dados = list()
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    count += 1
    if count == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
    r = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if 'n' in r:
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {count} pessoas.')
print(f'O maior peso foi {maior:.2f}Kg. Peso de ', end='')
for pos, pessoa in enumerate(pessoas):
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]',  end=' ')
print(f'\nO menor peso foi {menor:.2f}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
