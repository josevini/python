# Exercício 9.20 - Livro

agenda = []

def pedeNome():
    while True:
        nome = input('Nome: ')
        if nome.isalpha():
            return nome
        else:
            print('Apenas letras são permitidas!')

def pedeTelefone():
    while True:
        telefone = input('Telefone: ')
        if telefone.isnumeric():
            return telefone
        else:
            print('Apenas números são permitidos!')

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
    for p, e in enumerate(agenda):
        print(f'Contato: {p+1}', end=' ')
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

def ordena():
    fim = len(agenda)
    while True:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break

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
7 - Ordena
0 - Sai""")
    return validaFaixaInteiro('Escolha uma opção: ', 0, 7)

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
    elif opcao == 7:
        ordena()
menu()
