# Exercício 9.10 - Livro

import sys
args = sys.argv
files = args[1:]
content = ''
for filename in files:
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            content += file.read()
            with open('txt/saida.txt', 'w', encoding='UTF-8') as newFile:
                newFile.write(content)
    except FileNotFoundError as error:
        print('Arquivo não encontrado!\n')
