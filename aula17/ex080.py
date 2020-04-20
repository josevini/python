valores = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if len(valores) == 0:
        print('Primeiro valor adicionado!')
        valores.append(v)
    else:
        if v < min(valores):
            valores.insert(0, v)
            print('Adicionado na posição 0 da lista...')
        elif v > max(valores):
            print('Adicionado no final da lista...')
            valores.append(v)
        else:
            pos = 0
            while pos < len(valores):
                if v <= valores[pos]:
                    print(f'Adicionado na posição {pos} da lista...')
                    valores.insert(pos, v)
                    break
                pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
