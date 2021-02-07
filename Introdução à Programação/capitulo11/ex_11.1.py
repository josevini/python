# Exercício 11.1 - Livro

import sqlite3
from contextlib import closing

with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('insert into produto values (?, ?, ?)', ('4', 'desktop', '2460.77'))
