# Exercício 9.13 - Livro

import sys

args = sys.argv
if len(args) != 4:
    print('Formato: [filename] [start] [end]')
else:
    filename = args[1]
    start = args[2]
    end = args[3]
    if start < end:
        try:
            file = open(f'txt/{filename}', 'r', encoding='utf-8')
            content = file.readlines()
            for line in range(int(start), int(end)):
                print(f'{content[line]}')
            file.close()
        except FileNotFoundError:
            print('Arquivo não encontrado!')
        except IndexError:
            print('Fim da lista.')
    else:
        print('Início não pode ser maior que o fim.')
