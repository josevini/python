# Exercício 3.14 - Livro
km_percorrido = float(input('Quantos km o carro percorreu? '))
dias_uso = int(input('Por quantos dias o carro foi usado? '))
valor_total = (dias_uso * 60) + (km_percorrido * 0.15)
print(f'O valor total é de R${valor_total:.2f}')
