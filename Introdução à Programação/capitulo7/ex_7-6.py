# Exercício 7.6 - Livro

s1 = str(input('String 1: ')).upper()
s2 = str(input('String 2: ')).upper()
s3 = str(input('String 3: ')).upper()
if len(s2) == len(s3):
    res = ''
    for l in s1:
        pos = s2.find(l)
        if pos >= 0:
            res += s3[pos]
        else:
            res += l
    print(f'Resultado: {res}')
else:
    print('ERRO')
