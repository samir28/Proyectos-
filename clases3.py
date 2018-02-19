#Plantear una clase Club y otra clase Socio.
#La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
#En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
#La clase Club debe tener como atributos 3 objetos de la clase Socio.
#Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.

class Socio:

    def __init__(self):

        self.nombre = input("Ingrese el nombre: ")
        self.antiguedad= input("Ingrese su antiguedad: ")

    def imprimir(self):
        print(self.nombre, "tiene una antiguedad de ", self.antiguedad)
    def retorna_anti(self):
        return self.antiguedad

class Club:

    def __init__(self):

        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayor_anti(self):
        print("Socio de mayor antiguedad")
        if(self.socio1.retorna_anti() > self.socio2.retorna_anti() and self.socio1.retorna_anti() > self.socio3.retorna_anti()):
            self.socio1.imprimir()
        else:
            if(self.socio2.retorna_anti() > self.socio3.retorna_anti()):
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()

#bloque principal

club= Club()
club.mayor_anti()
