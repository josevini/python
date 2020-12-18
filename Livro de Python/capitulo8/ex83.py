# Exercício 8.13 - Livro

import random
comp = random.randint(1, 10)
tentativas = 3
while tentativas > 0:
    try:
        print('---' * 10)
        print(f'{tentativas}', 'tentativas restantes' if tentativas > 1 else 'tentativa restante')
        num = int(input('Digite um valor entre 1 e 10: '))
        print('---' * 10)
        if num == comp:
            print('Você acertou!')
            break
        else:
            print('Você não acertou!')
        tentativas -= 1
    except Exception as excecao:
        print(f'Alerta de exceção: {excecao}')
