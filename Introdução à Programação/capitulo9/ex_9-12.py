# Exercício 9.12 - Livro

import sys

if len(sys.argv) != 2:
    print("\nUso: e09-12.py arquivo1\n\n\n")
    sys.exit(1)

name = sys.argv[1]
count = {}
lin = 1
col = 1

file = open(f'txt/{name}', 'r', encoding='utf-8')
for line in file:
    line = line.strip().lower()
    words = line.split(' ')
    for p in words:
        if p == '':
            col += 1
            continue
        if p in count:
            count[p].append((lin, col))
        else:
            count[p] = [(lin, col)]
        col += len(p) + 1
    lin += 1
    col = 1
file.close()

for key in count:
    print(f'{key} = {count[key]}')
