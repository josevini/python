# Exercício 9.2 - Livro

import sys
args = sys.argv
if len(args) != 4:
    print(f'Dica: {args[0]} arquivo início fim')
else:
    inicio = args[2]
    fim = args[3]
    nome = args[1]
    file = open(nome, 'r')
    for linha, dado in enumerate(file.readlines()):
        if (linha + 1) >= int(inicio) and (linha + 1) <= int(fim):
            print(dado)
    file.close()
