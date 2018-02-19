def carga():
    agenda = {}
    continuas1 = "s"
    while continuas1 == "s":
        fecha = input("ingrese la fecha de la actividad: ")
        continuas2 = "s"
        lista = []
        while continuas2 == "s":
            hora = input("ingrese la hora: ")
            actividad = input("ingrese la actividad: ")
            lista.append((hora, actividad))
            continuas2 = input("ingresar otra actividad: [S/N]")
            agenda[fecha] = lista
            continuas1 = input("ingresar otra fecha: [S/N]")
        return agenda

def imprimir(agenda):
    print("listado completo de actividades: ")
    for fecha in agenda:
        print("para la fecha: ", fecha)
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def consulta(agenda):
    fecha = input("ingrese la fecha que desea: ")
    if fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)
    else:
        print("no hay actividades agendadas")


#bloque principal

agenda = carga()
imprimir(agenda)
consulta(agenda)

    
