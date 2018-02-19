class Cuenta:

    def __init__(self, monto, titular):

        self.titular= titular
        self.monto= monto
    def imprimir(self):
        print("Titular: ", self.titular)
        print("Monto: ", self.monto)

class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interese):
        
        super().__init__(titular, monto)
        self.plazo= plazo
        self.interese= interese

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en dias: ", self.plazo)
        print("Interes: ", self.interese)
        self.ganancia_interese()
        
    def ganancia_interese(self):
        ganancia= self.monto * self.interese/100
        print("Importe del interese: ", ganancia)

#bloque principal

cajaahorro= CajaAhorro("Juan", 2000)
cajaahorro.imprimir()

plazofijo= PlazoFijo("Diego", 10000, 30, 0.75)
plazofijo.imprimir()

        
    
        
