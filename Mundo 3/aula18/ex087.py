matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(v)
print('-=' * 30)
