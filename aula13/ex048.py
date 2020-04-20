s = 0
v = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        v += 1

print(f'A soma de todos os {v} valores é {s}')
