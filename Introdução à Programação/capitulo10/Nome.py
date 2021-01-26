class Nome:
    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
