# Exercício 10.4 - Livro

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

tv = Televisao()
tv.volta()
print(f'Canal atual: {tv.canal}')
