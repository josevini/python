# Exercício 10.9 - Livro

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
    def populacaoTotal(self):
        popTotal = 0
        for cidade in self.cidades:
            popTotal += cidade.populacao
        print(f'{self.nome} tem um total de {popTotal} habitantes')
    def populacaoIndividual(self):
        print('-' * 25)
        for cidade in self.cidades:
            print(f'{cidade.nome:<16} {cidade.populacao}')
        print('-' * 25)

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

maceio = Cidade('Maceió', 1_038_948)
arapiraca = Cidade('Arapiraca', 231_747)
rio_largo = Cidade('Rio Largo', 75_120)

al = Estado('Alagoas', 'AL', [maceio, arapiraca, rio_largo])
al.populacaoIndividual()
al.populacaoTotal()
