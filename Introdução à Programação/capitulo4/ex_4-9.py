# Exercício 4.9 - Livro

preco = float(input('Preço da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Anos para pagar a casa: '))

valor_mensal = preco / (anos * 12)
parte_salario = (salario * 30) / 100

print('=-=' * 8)
print(f'Valor mensal: {valor_mensal:.2f}')
print(f'30% do salário: {parte_salario:.2f}')
print('=-=' * 8)

if valor_mensal > parte_salario:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
