# Exercício 8.7 - Livro
def mdc(a, b):
    if b == 0:
        return a
    print(f'{a} {b}')
    return mdc(b, (a % b))
print(mdc(18, 60))
