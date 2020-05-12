matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        n = int(input(f'Digite um valor para [{lin}, {col}]: '))
        matriz[lin].append(n)
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end=' ')
    print('')
