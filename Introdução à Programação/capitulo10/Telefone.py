import listaUnica
import Nome
import tipoTelefone

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

class tiposTelefones(listaUnica):
    def __init__(self):
        super().__init__(tipoTelefone)


