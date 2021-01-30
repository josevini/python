# Exercício 6.6 - Livro

ult1 = 0
ult2 = 0
sair = False
fila1 = [] # a → atender; f → adicionar; s → sair
fila2 = [] # b → atender; g → adicionar; s → sair
while True:
    print('=-=' * 15)
    print(f'Fila 1: {fila1}')
    print(f'Fila 2: {fila2}')
    print('=-=' * 12)
    print("""(A) - Atende um cliente na fila 1
    (F) - Adiciona um cliente na fila 1
    (B) - Atende um cliente na fila 2
    (G) - Adiciona um cliente na fila 2
    (S) - Sai de ambas filas""")
    print('=-=' * 12)
    op = str(input('Informe a operação desejada: '))
    final_comando = len(op)
    pos = 0
    while pos < final_comando:
        if op[pos] == 'S' or op[pos] == 's':
            sair = True
        elif op[pos] == 'A' or op[pos] == 'a':
            if len(fila1) == 0:
                print(f'A fila 1 está vazia')
            else:
                fila1.pop(0)
        elif op[pos] == 'F' or op[pos] == 'f':
            ult1 += 1
            fila1.append(ult1)
        elif op[pos] == 'B' or op[pos] == 'b':
            if len(fila2) == 0:
                print(f'A fila 2 está vazia')
            else:
                fila2.pop(0)
        elif op[pos] == 'G' or op[pos] == 'g':
            ult2 += 1
            fila2.append(ult2)
        else:
            print('Opção inválida!')
        pos += 1
    if sair == True:
        break
