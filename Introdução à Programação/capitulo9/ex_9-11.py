# Exercício 9.11 - Livro

import sys
args = sys.argv[1:]
dic = dict()
key = ''
value = 0
if len(args) > 1:
    print('Informe um único arquivo!')
else:
    filename = args[0]
    try:
        with open(f'txt/{filename}', 'r', encoding='UTF-8') as file:
            content = file.read().split()
            for word in content:
                key, value = word, content.count(word)
                dic[key] = value
            print(dic)
    except FileNotFoundError as error:
        print('Arquivo não encontrado!\n')
