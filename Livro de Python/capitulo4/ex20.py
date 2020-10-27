# Exercício 4.10 - Livro

tipo = str(input('Tipo de instalação: '))
faixa = float(input('Faixa desejada: '))
preco = 0

if tipo == 'r':
    if faixa <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'c':
    if faixa <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'i':
    if faixa <= 5000:
        preco = 0.55
    else:
        preco = 0.60
valor = preco * faixa
print(f'Valor total: {valor:.2f}')
