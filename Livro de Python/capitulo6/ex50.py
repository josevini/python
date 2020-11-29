# Exercício 6.7 - Livro

exp = str(input('Informe uma expressão com parênteses: '))
pilha = []
tamanho = len(exp)
pos = 0
while pos < tamanho:
    if exp[pos] == '(':
        pilha.append('(')
    if exp[pos] == ')':
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(')')
            break
    pos += 1
if len(pilha) == 0:
    print('OK')
else:
    print('ERRO')
