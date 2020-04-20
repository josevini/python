n = int(input('Digite um número: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        div += 1
        print('\033[0;33m', c, '\033[m',  end='')
    else:
        print('\033[0;31m', c, '\033[m', end='')
print(f"""\nO número {n} foi divisível {div} veze(s)
E por isso ele """, end='')
if div == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
