# Exercício 5.14 - Livro


soma = media = 0
qtd = 0
while True:
    num = int(input(f'Digite o {qtd + 1}° número: '))
    if num == 0:
        break
    qtd += 1
    soma += num
media = soma / qtd
print('=-=' * 15)
print(f'Quantidade de números informados: {qtd}')
print(f'Soma de todos os valores: {soma}')
print(f'Média dos valores: {media:.2f}')
