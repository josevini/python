menos_de_20 = total_homem = mais_de_18 = 0

while True:
    print('-' * 27)
    print('\tCADASTRE UMA PESSOA')
    print('-' * 27)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 27)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        mais_de_18 += 1
    if sexo == 'M':
        total_homem += 1
    if sexo == 'F' and idade < 20:
        menos_de_20 += 1
    if opcao == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {mais_de_18}')
print(f'Ao todo temos {total_homem} homens cadastrados')
print(f'E temos {menos_de_20} mulheres com menos de 20 anos')

