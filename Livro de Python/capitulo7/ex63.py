# Exercício 7.2 - Livro

s1 = str(input('String 1/3: ')).upper()
s2 = str(input('String 2/3: ')).upper()
s3 = ''
for v in s1:
    if v in s2:
        s3 += v
print(f'String 3/3: {s3}')
