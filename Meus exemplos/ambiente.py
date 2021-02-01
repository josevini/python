import os
import os.path

def desenha(simb='', qtd=0):
    print(simb * qtd)

def mensagem(msg='', char='-'):
    desenha(char, len(msg) * 3)
    print(f'{msg.center(len(msg) * 3)}')
    desenha(char, len(msg) * 3)

def entradaTexto(msg=''):
    valor = input(msg)
    return valor

def pergunta(msg=''):
    resp = input(msg).lower()[0]
    if resp == 's':
        return True
    return False

def entrada(msg=''):
    while True:
        valor = input(msg)
        try:
            return int(valor)
        except Exception as erro:
            print('Digite um número válido!')
def intervalo(valor, min, max):
    if min <= valor <= max:
        return valor
    print(f'Digite um valor entre {min} e {max}')

def criar():
    desenha('-', 42)
    print("""Deseja criar um arquivo ou uma pasta?
1 - Arquivo
2 - Pasta
0 - Cancelar""")
    desenha('-', 42)
    op = intervalo(entrada('Escolha uma opção: '), 0, 2)
    if op == 0:
        print('Cancelado...')
    elif op == 1:
        filename = entradaTexto('Informe o nome do arquivo: ')
        grava = pergunta('Habilitar edição de arquivo? [s/n]: ')
        nome, ext = os.path.splitext(filename)
        file = open((nome+ext) if ext else (nome+'.txt'), 'w' if grava else 'r', encoding='utf-8')
    elif op == 2:
        dirname = entradaTexto('Informe o nome da pasta: ')


while True:
    mensagem('MENU PRINCIPAL')
    print("""1 - Criar
2 - Apagar
3 - Acessar
4 - Editar
0 - Sair""")
    desenha('-', 42)
    op = intervalo(entrada('Escolha uma opção: '), 0, 4)
    if op == 0:
        break
    elif op == 1:
        criar()

