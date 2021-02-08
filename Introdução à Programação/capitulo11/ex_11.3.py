# Exercício 11.3 - Livro

import sqlite3
from contextlib import closing

prod = str(input('Informe o nome do produto: '))
with sqlite3.connect('db/preco.db') as connection:
    with closing(connection.cursor()) as cursor:
        result = cursor.execute('select * from produto where nome = ?', (prod,)).fetchone()
        if result:
            print(result)
        else:
            print('Nada encontrado!')
