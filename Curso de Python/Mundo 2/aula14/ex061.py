print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(p1, end=' → ')
    p1 += r
    c += 1
print('FIM')
