# Exercício 9.9 - Livro

files = ['txt/file1.txt', 'txt/file2.txt', 'txt/file3.txt']
for filename in files:
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            print(file.read())
    except FileNotFoundError as error:
        print('Arquivo não encontrado!\n')
