# Exercício 11.4 - Livro

import sqlite3
from contextlib import closing

min = float(input('Digite um preço mínimo: '))
max = float(input('Digite o preço máximo: '))
with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        result = cursor.execute(f'select * from produto where preco >= {min} and preco <= {max}').fetchall()
