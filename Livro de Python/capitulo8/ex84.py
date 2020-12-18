# Exercício 8.14 - Livro
from random import choice
palavras = []
while True:
    if len(palavras) == 5:
        break
    p = str(input(f'Digite a {len(palavras) + 1}° palavra: ')).lower().strip()
    palavras.append(p)
palavra = choice(palavras)
for x in range(100):
    print()
digitados = []
acertos = []
erros = 0
while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        break
    tentativa = str(input('\nDigite uma letra: ')).lower().strip()
    if tentativa in digitados:
        print('Você já tentou essa letra!')
        continue
    else:
        digitados += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    print('X==:==\nX : ')
    print('X O ' if erros >= 1 else 'X')
    linha2 = ''
    if erros == 2:
        linha2 = ' | '
    elif erros == 3:
        linha2 = ' \| '
    elif erros == 4:
        linha2 = ' \|/ '
    print(f'X{linha2}')
    linha3 = ''
    if erros == 5:
        linha3 += ' / '
    elif erros >= 6:
        linha3 = ' /\ '
    print(f'X{linha3}')
    print('X\n===========')
    if erros == 6:
        print('Enforcado!')
        break
