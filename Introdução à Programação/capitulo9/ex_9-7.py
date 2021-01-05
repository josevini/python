# Exercício 9.7 - Livro
from functions import *

with open('txt/arquivo_paginas.txt', encoding='UTF-8') as file:
    filename = getFilename(file.name)
    text = file.read().split()
    lineCount = pageCount = 1
    line = msg = ''
    maxLength = 76
    with open('txt/novo_arquivo.txt', 'w', encoding='UTF-8') as newFile:
        for word in text:
            msg = f'{word} '
            if maxLength - len(line) >= len(msg):
                line += msg
            else:
                newFile.write(f'{line}\n')
                lineCount += 1
                if lineCount % 60 == 0:
                    newFile.write(f' == Página {pageCount} → {filename} == \n')
                    pageCount += 1
                line = f'{msg}'
