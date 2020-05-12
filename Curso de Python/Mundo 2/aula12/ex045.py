from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções: ')
print("""[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
computador = randint(0,2)
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0 and jogador == 1 or computador == 2 and jogador == 0 or computador == 1 and jogador == 2:
    print('JOGADOR VENCE')
elif jogador == 0 and computador == 1 or jogador == 2 and computador == 0 or jogador == 1 and computador == 2:
    print('COPUTADOR VENCE')
elif jogador == computador:
    print('EMPATE')
else:
    print('Opção inválida')
