# Exercício 10.2 - Livro

class Televisao:
    def __init__(self, canal):
        self.ligada = False
        self.canal = canal
        self.tamanho = 0
        self.marca = ''

t1 = Televisao(7)
print(t1.canal)
