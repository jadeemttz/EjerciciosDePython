class Descuento:
    def __init__(self, mes, importe):
        self.mes = mes
        self.importe = importe

    def calcular_total(self):
        if self.mes == 10:
            return self.importe * 0.85  
        return self.importe
