# Exercício 10.1 - Livro

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0
        self.tamanho = 0
        self.marca = ''
t1 = Televisao()
t1.tamanho = 32
t1.marca = 'AOC'
print(f'TV {t1.marca} de {t1.tamanho} polegadas')

t2 = Televisao()
t2.tamanho = 42
t2.marca = 'Samsnug'
print(f'TV {t2.marca} de {t2.tamanho} polegadas')
