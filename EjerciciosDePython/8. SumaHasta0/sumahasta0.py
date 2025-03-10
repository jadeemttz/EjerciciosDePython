class Sumador:
    def __init__(self):
        self.suma_total = 0

    def agregar_numero(self, numero):
        self.suma_total += numero
        return self.suma_total
