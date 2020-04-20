from random import randint
tentativas = 1
comp = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advivinhar qual foi? ')
num = int(input('Qual é seu palpite? '))

while num != comp:
    if num < comp:
        print('Mais... Tente mais uma vez.')
    if num > comp:
        print('Menos... Tente mais uma vez.')
    num = int(input('Qual é o seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
