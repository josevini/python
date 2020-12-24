# Exercício 5.10 - Livro

pontos = 0
questao = 1
while questao <= 3:
    res = str(input(f'Resposta da questão {questao}: '))
    if questao == 1 and (res == 'b' or res == 'B'):
        pontos += 1
    elif questao == 2 and (res == 'a' or res == 'A'):
        pontos += 1
    elif questao == 3 and (res == 'd' or res == 'D'):
        pontos += 1
    questao += 1
print(f'O aluno fez {pontos} pontos.')
