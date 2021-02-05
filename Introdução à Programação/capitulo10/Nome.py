from functools import total_ordering
import listaUnica

@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f'<Classe {type(self).__name__} em 0x{id(self):x} em Nome: {self.__nome} Chave: {self.__chave}>'
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
        self.__chave = Nome.criaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()

class Telefone:
    def __init__(self, num, tipo=None):
        self.numero = num
        self.tipo = tipo
    def __str__(self):
        if self.tipo is not None:
            tipo = self.tipo
        else:
            tipo = ''

    def __eq__(self, other):
        return self.numero == other.numero and ((self.tipo == other.tipo) or (self.tipo is None or other.tipo is None))
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor is None or not valor.strip():
            raise ValueError('Número não pode ser None ou em branco')
        self.__numero = valor

class Telefones(listaUnica):
    def __init__(self):
        super().__init__(Telefone)

class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):
            raise TypeError('Nome não deve ser uma instância da classe Nome')
        self.__nome = valor
    def pesquisaTelefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]

