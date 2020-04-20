from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
valores = (n)
print(f'Os valores sorteados foram {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
