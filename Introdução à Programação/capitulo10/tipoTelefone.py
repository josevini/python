from functools import total_ordering

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return f'({self.tipo}) '
    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.tipo == other.tipo
    def __lt__(self, other):
        return self.tipo < other.tipo
