l1 = [1, 3, 5, 6, 7, 5, 6, 10]
l2 = [2, 4, 5, 6, 8, 1, 2, 5]
inter = set(l1).intersection(l2)
dif = set(l1).difference(l2)
print(f'Valores comuns: {list(inter)}')
print(f'Elementos da l1: {l1}')
print(f'Elementos da l2: {l2}')
l3 = set(l1 + l2)
print(f'l1 e l2 sem repetições: {list(l3)}')
