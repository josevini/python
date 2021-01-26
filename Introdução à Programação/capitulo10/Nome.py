from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f'<Classe {type(self).__name__} em 0x{id(self):x} em Nome: {self.nome} Chave: {self.chave}>'
    def __eq__(self, outro):
        print('__eq__ chamado')
        return self.nome == outro.nome
    def __lt__(self, outro):
        print('__lt__ chamado')
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if valor is None or not valor.strip():
            raise TypeError('Nome não pode ser nulo ou em branco.')
        self.__nome = valor
        self.__nome = Nome.criaChave(valor)
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()
