n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO.')
elif m < 5:
    print('O aluno está REPROVADO.')
elif m >= 5 and m <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
