class IndexErradoException(Exception):
    def __init__(self):
        super().__init__("O index não existe!")

class TelaInvalidaException(Exception):
    def __init__(self):
        super().__init__("A tela desejada não existe!")