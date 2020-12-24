# Exercício 5.22 - Livro

while True:
    print('=-=' * 7)
    print("""\t\tMenu
    (1) - Adição
    (2) - Subtração
    (3) - Divisão
    (4) - Multiplicação
    (5) - Sair""")
    print('=-=' * 7)
    opc = int(input('Informe a operação desejada: '))
    if opc == 5:
        break
    valor = int(input('Informe o valor para ver a tabuada: '))
    cont = 1
    while cont <= 10:
        if opc == 1:
            print(f'{valor} + {cont} = {valor + cont}')
        elif opc == 2:
            print(f'{valor} - {cont} = {valor - cont}')
        elif opc == 3:
            print(f'{valor} / {cont} = {valor / cont}')
        elif opc == 4:
            print(f'{valor} x {cont} = {valor * cont}')
        else:
            print('Opção inválida!')
        cont += 1

