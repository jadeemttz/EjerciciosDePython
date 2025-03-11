class DescuentoEntrada:
    def __init__(self, edad):
        self.edad = edad
        self.precio_base = 50  

    def calcular_pago(self):
        if self.edad < 10:
            return self.precio_base * 0.75 
        return self.precio_base
