# Exercício 10.5 - Livro

class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.minimo = min
        self.maximo = max
        self.tamanho = 0
        self.marca = ''
    def avanca(self):
        print('Muda canal!')
        if self.minimo <= self.canal < self.maximo:
            self.canal += 1
        else:
            self.canal = self.minimo
    def volta(self):
        print('Muda canal!')
        if self.maximo >= self.canal > self.minimo:
            self.canal -= 1
        else:
            self.canal = self.maximo

tv1 = Televisao(min=1, max=10)
print(f'TV1 mínimo: {tv1.minimo} máximo: {tv1.maximo}')

tv2 = Televisao(min=2, max=20)
print(f'TV2 mínimo: {tv2.minimo} máximo: {tv2.maximo}')
