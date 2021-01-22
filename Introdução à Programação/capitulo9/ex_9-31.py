# Exercício 9.31 - Livro

import os.path
chave = str(input('Buscar diretório/arquivo: '))
encontrado = os.path.exists(chave)
if encontrado:
    obj = ''
    if os.path.isdir(chave):
        obj = 'diretório'
    else:
        obj = 'arquivo'
    print(f'{obj.capitalize()} encontrado!')
else:
    print('Arquivo ou Diretório não encontrado!')
