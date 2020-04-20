print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))

print('~' * 30)
inicio = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' → ')
fim = termos
while inicio <= fim:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    inicio += 1
print('FIM')
