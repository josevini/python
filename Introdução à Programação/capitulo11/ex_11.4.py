# Exercício 11.4 - Livro

import sqlite3
from contextlib import closing

with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        result = cursor.execute('select * from produto where').fetchall()
