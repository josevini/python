# Exercício 9.14 - Livro

import sys
from functions import removeSpaces, removeEmptyLine

args = sys.argv
if len(args) != 2:
    print('Formato: [filename]')
else:
    filename = args[1]
    path = f'txt/{filename}'
    file = open(path, 'r', encoding='utf-8')
    content = removeSpaces(removeEmptyLine(file.readlines()))
    file.close()
