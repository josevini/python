# Exercício 5.27 - Livro

num = str(input('Digite um número: '))
novo_num = ''
pos = (len(num) - 1)
total = 0
while pos >= total:
    novo_num += num[pos]
    pos -= 1
if novo_num == num:
    print(f'{num} é um palíndromo!')
else:
    print(f'{num} não é um palíndromo!')
