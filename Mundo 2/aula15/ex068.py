from random import randint
vitorias = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    computador = randint(1, 10)
    jogada = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-' * 30)
    valor = jogada + computador
    if valor % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'
    print(f'Você jogou {jogada} e o computador {computador}. Total de {valor} DEU {res}')
    print('-' * 30)
    if (opcao == 'P' and res == 'PAR') or (opcao == 'I' and res == 'ÍMPAR'):
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        break
print(f'GAME OVER! Você venceu {vitorias} vez(es)!')
