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
