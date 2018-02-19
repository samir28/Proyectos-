class Agenda:

    def __init__(self):
        self.contactos = {} #definimos un diccionario

    def menu(self):
        opcion=0
        while opcion != 5:
            print("1 - Cargar un contacto en la agenda")
            print("2 - Listado completo de la agenda")
            print("3 - Consulta ingresando el nombre de la persona")
            print("4 - Modificacion del telefono y mail")
            print("5 - Finalizar el programa")
            opcion = int(input("Ingrese su opcion: "))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()
        

    def cargar(self):
        nombre= input("Ingrese el nombre de la persona: ")
        telefono= input("Ingrese el numero de telefono: ")
        mail= input("Ingrese el E-mail: ")
        self.contactos[nombre] = (telefono, mail)
        print("_________________________________")

    def listado(self):
        print("________________")
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
            print("__________________")

    def consulta(self):
        print("__________________")

        nombre = input("Ingrese el nombre para la consulta: ")
        if nombre in self.contactos:
            print(nombre, "su telefeno es ", self.contactos[nombre][0],"y su mail es ", self.contactos[nombre][1])
        else:
            print("no existe el contacto con ese nombre")

    def modificacion(self):
        print("____________________")

        nombre= input("Ingrese el nombre a modificar: ")
        if nombre in self.contacto:
            telefono= int(input("Ingrese el nuevo telefono: "))
            mail= input("Ingrese su nuevo mail: ")
            self.contactos[nombre] = (telefono, mail)
        else:
            print("No existe un contacto con ese nombre")
        print("___________________")


#bloque principal

agenda = Agenda()
agenda.menu()

            
    
            
            



        
