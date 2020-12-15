# Exercício 8.13 - Livro

def letraValida(op):
    str(op.lower())
    while True:
        v = input('Digite uma letra: ').lower()
        if v not in op:
            print('Tente novamente!')
            continue
        else:
            break

letraValida('mf')
