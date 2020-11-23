# Exercício 6.5 - Livro

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print('=-=' * 20)
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila')
    print('ou A para realizar o atendimento. S para sair.')
    op = str(input('Operação: '))
    if op == 'S' or op == 's':
        break
    elif op == 'F' or op == 'f':
        ultimo += 1
        fila.append(ultimo)
    elif op == 'A' or op == 'a':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia')
    else:
        print('Informe uma operação válida!')
