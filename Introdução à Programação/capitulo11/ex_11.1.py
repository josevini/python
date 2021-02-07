# Exercício 11.1 - Livro

import sqlite3
from contextlib import closing

with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        # cursor.execute('insert into produto values (?, ?, ?)', ('3', 'tablet', '320.90'))
        reg = cursor.execute('select * from produto')
        while reg.fetchone():
            print(reg.fetchone())
