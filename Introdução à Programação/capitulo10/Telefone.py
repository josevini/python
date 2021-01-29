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
