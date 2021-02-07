# Exercício 11.2 - Livro

import sqlite3
from contextlib import closing

with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        result = cursor.execute('select * from produto').fetchall()
        for reg in result:
            print(f'{reg[1]} {reg[2]}')
