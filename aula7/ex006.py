from math import sqrt
from time import sleep
num = int(input('Digite um número: '))
print('Analisando...')
sleep(2)
print("""Dobro: {}
Triplo: {}
Raiz quadrada: {:.2f}""".format(num * 2, num * 3, sqrt(num)))
