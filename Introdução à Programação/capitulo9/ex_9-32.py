# Exercício 9.32 - Livro

import os.path, sys

args = sys.argv
if len(args) == 2:
    chave = args[1]
    encontrado = os.path.exists(chave)
    if encontrado:
        if os.path.isdir(chave):
            obj = 'diretório'
        else:
            obj = 'arquivo'
        print(f'{obj.capitalize()} encontrado!')
    else:
        print('Arquivo ou Diretório não encontrado!')
else:
    print('Erro!')
