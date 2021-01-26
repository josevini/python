# Exercício 3.10 - Livro
salario = float(input('Informe seu salário | R$'))
aumento = int(input('Aumento de quantos porcento? '))
valor_aumento = ((salario * aumento) / 100)
novo_salario = salario + valor_aumento
print('=-=' * 10)
print(f"""Salário atual → {salario}
Valor do aumento → {valor_aumento}
Novo salário → {novo_salario}""")
