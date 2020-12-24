# Exercício 3.15 - Livro
import math
cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))
dias_perdidos = ((cigarros * 10) * (anos * 3650) / 1440)
print(f'No total, você perdeu, aproximadamente, {math.ceil(dias_perdidos)} dias.')
