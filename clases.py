class Estudiante:

    def __init__(self):
        self.carrera = []
        self.legajo = []

    def menu(self):
        opcion=0
        while opcion !=4:
            print("1- cargar Estudiante")
            print("2- listar Estudiante")
            print("3- Finalizar programa")
            opcion = int(input("\n Ingrese su opcion: "))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()

    def cargar(self):
        for x in range(5):
            car= input("Ingrese la carrera: ")
            self.carrera.append(car)
            leg= int(input("Ingrese su legajo: "))
            self.legajo.append(leg)

    def listar(self):
        print("listado completo de los estudiantes")
        for x in range(5):
            print("Carrera: ", self.carrera[x])
            print("Legajo: ",self.legajo[x])
        print("------------")


#bloque main
alumno = Estudiante()
alumno.menu()
