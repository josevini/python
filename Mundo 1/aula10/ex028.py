from time import sleep
from random import randint
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
comp = randint(0, 5)
num = int(input('Em que número eu pensei? '))
if num == comp:
    print('PROCESSANDO...')
    sleep(2)
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('PROCESSANDO...')
    sleep(2)
    print('GANHEI! Eu pensei no número {} e não no {}'.format(comp, num))

