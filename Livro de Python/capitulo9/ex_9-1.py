# Exercício 9.1 - Livro

import sys
arg = sys.argv
if len(arg) != 2:
    print('Você precisa informar um arquivo para fazer a leitura.')
else:
    file = open(arg[1], 'r')
    print(file.read())
    file.close()
