# Exercício 6.5 - Livro

ultimo = 10
fila = list(range(1, ultimo + 1))
sair = False
while True:
    print('=-=' * 20)
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila')
    print('ou A para realizar o atendimento. S para sair.')
    op = str(input('Operação: '))
    tot = len(op)
    pos = 0
    while pos < tot:
        if op[pos] == 'S' or op[pos] == 's':
            sair = True
        elif op[pos] == 'F' or op[pos] == 'f':
            ultimo += 1
            fila.append(ultimo)
        elif op[pos] == 'A' or op[pos] == 'a':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Fila vazia')
        else:
            print('Informe uma operação válida!')
        pos += 1
    if sair:
        break
