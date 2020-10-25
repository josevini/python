# Exercício 4.4 - Livro

sal = float(input('Salário: '))
aumento = 0
if sal > 1250:
    aumento = (sal * 10) / 100
if sal <= 1250:
    aumento = (sal * 15) / 100
sal += aumento
print(f'Novo salário: {sal}')
