s = 0
v = 0
for c in range(1, 7, 1):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
        v += 1
print(f'A soma de todos os {v} valores vale {s}')
