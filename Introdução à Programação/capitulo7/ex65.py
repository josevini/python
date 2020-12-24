# Exercício 7.4 - Livro

s = str(input('String 1/1: ')).upper()
validado = ''
for l in s:
    if l not in validado:
        print(f'{l} → {s.count(l)}x')
        validado += l

