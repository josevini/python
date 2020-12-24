# Exercício 5.8 - Livro

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
cont = 1
res = 0
while cont <= num2:
    res += num1
    cont += 1
print(f'{num1} x {num2} = {res}')
