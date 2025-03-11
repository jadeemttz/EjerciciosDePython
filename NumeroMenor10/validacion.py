class ValidacionNumero:
    def __init__(self, numero):
        self.numero = numero

    def es_valido(self):
        return self.numero < 10
