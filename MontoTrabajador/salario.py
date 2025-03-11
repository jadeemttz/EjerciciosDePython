class Empleado:
    def __init__(self, nombre, horas_normales, horas_extras, hijos, tarifa_hora):
        self.nombre = nombre
        self.horas_normales = horas_normales
        self.horas_extras = horas_extras
        self.hijos = hijos
        self.tarifa_hora = tarifa_hora

    def calcular_monto_normales(self):
        return self.horas_normales * self.tarifa_hora

    def calcular_monto_extras(self):
        return self.horas_extras * (self.tarifa_hora * 1.5)

    def calcular_bonificacion(self):
        return self.hijos * 0.5

    def calcular_pago_total(self):
        return self.calcular_monto_normales() + self.calcular_monto_extras() + self.calcular_bonificacion()
