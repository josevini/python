# Exercício 9.17 - Livro

agenda = []

def pedeNome():
    return input('Nome: ')

def pedeTelefone():
    return input('Telefone: ')

def mostraDados(nome, telefone):
    print(f'Nome: {nome} Telefone: {telefone}')

def pedeNomeArquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda
    nome = pedeNome()
    telefone = pedeTelefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pedeNome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print('Nome não encontrado!')

def altera():
    p = pesquisa(pedeNome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado: ')
        mostraDados(nome, telefone)
        nome = pedeNome()
        telefone = pedeTelefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado!')

def lista():
    print('\nAgenda\n\n-------')
    for e in agenda:
        mostraDados(e[0], e[1])
    print('-------\n')

def lê():
    global agenda
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])

def grava():
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

def validaFaixaInteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')

def tamanhoLista():
    return len(agenda)

def menu():
    print(f'{tamanhoLista()} contato(s)')
    print("""1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
0 - Sai""")
    return validaFaixaInteiro('Escolha uma opção: ', 0, 6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        lê()
menu()
