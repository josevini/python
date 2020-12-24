# Exercício 9.4 - Livro

import sys
args = sys.argv
total_args = len(args)
if total_args != 3:
    print(f'O programa precisa de dois argumentos: nome1 nome2')
else:
    arq1 = args[1]
    arq2 = args[2]
    try:
        with open('file3.txt', 'w', encoding='UTF-8') as f3, open(arq1, 'r', encoding='UTF-8') as f1, open(arq2, 'r', encoding='UTF-8') as f2:
            txt1 = f1.read()
            txt2 = f2.read()
            f3.write(str(txt1))
            f3.write(str(txt2))
    except FileNotFoundError as excecao:
        print('Um ou mais arquivos não existem!')
