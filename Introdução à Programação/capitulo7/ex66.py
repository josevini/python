# Exercício 7.5 - Livro

s1 = str(input('String 1/3: '))
s2 = str(input('String 2/3: '))
s3 = ''
for l in s1:
    if l not in s2:
        s3 += l
print(f'String 3/3: {s3}')
