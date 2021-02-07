# Exercício 11.1 - Livro

import sqlite3
from contextlib import closing

with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        insert = 'insert into produto values (?, ?, ?)'
        values = [('1', 'notebook', '1300.5'), ('2', 'celular', '900.5'), ('3', 'tablet', '320.6'), ('4', 'desktop', '2460.7')]
        # cursor.executemany(insert, values)
