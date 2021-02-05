import listaUnica
import tipoTelefone


class TiposTelefone(listaUnica):
    def __init__(self):
        super().__init__(tipoTelefone)

class Agenda(listaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()

