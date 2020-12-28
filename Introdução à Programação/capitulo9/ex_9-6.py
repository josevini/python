# Exercício 9.6 - Livro

with open('txt/entrada.txt', 'r') as entrada:
    linhas = entrada.readlines()
    for linha in linhas:
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(79))
        elif linha[0] == '<':
            print(linha[1:].ljust(79))
        elif linha[0] == '*':
            print(linha[1:].center(79))
        elif linha[0] == '=':
            print('=' * 40)
        elif linha[0] == '.':
            input('Digite algo para continuar ')
            print()
        else:
            print(linha)
