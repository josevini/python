print('='*30)
print('\t10 TERMOS DE UMA PA')
print('='*30)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    print(t1, end='→ ')
    t1 += r
print('ACABOU')
