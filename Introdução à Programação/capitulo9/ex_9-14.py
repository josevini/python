# Exercício 9.14 - Livro

import sys

args = sys.argv
if len(args) != 2:
    print('Formato: [filename]')
else:
    filename = args[1]
    path = f'txt/{filename}'
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    print(content)
    file.close()
