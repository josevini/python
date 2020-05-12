opc = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opc != 5:
    print("""\t[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opc = int(input('>>>>> Qual é a sua opção? '))
    if opc == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opc == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior valor é {maior}')
    elif opc == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 12)
