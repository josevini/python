# Exercício 4.8 - Livro

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
res = 0

print("=-=" * 10)
print("""(1) - Soma
(2) - Subtração
(3) - Divisão
(4) - Multiplicação""")
print("=-=" * 10)

op = int(input('Informe a operação desejada: '))
if op == 1:
    res = v1 + v2
elif op == 2:
    res = v1 - v2
elif op == 3:
    res = v1 / v2
elif op == 4:
    res = v1 * v2
else:
    print('Operação inválida!')
print(f'Resultado da operação: {res}')
