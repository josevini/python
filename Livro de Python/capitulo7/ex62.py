# Exercício 7.1 - Livro
s1 = str(input('Digite a primeira string: ')).upper()
s2 = str(input('Digite a segunda string: ')).upper()
pos = s1.find(s2)
if pos >= 0:
    print(f'{s2} encontrada na posição {pos}')
else:
    print('Nada foi encontrado!')
