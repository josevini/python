cont = 0
soma = 0
maior = 0
menor = 0
opc = ''
while opc != 'n':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    opc = str(input('Quer continuar? [S/N] ')).lower().strip()
    while opc != 'n' and opc != 's':
        print('Opção inválida! Tente novamente.')
        opc = str(input('Quer continuar? [S/N] ')).lower().strip()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
