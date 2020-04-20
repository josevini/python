count = 0
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    peso = float(input('Peso: '))
    count += 1
    r = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if 'n' in r:
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {count} pessoas.')
