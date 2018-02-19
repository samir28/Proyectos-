def carga():
    alumno = {}
    for x in range(3):
        dni = int(input("ingrese su dni: "))
        lista_materia = []
        continua = "s"
        while continua == "s":
            materia = input("ingrese el nombre de la materia: ")
            nota = int(input("ingrese su nota: "))
            lista_materia.append((materia, nota))
            continua = input("desea cargar otra materia: [S/N]")
            alumno[dni] = lista_materia
        return alumno

def listar(alumno):
    for dni in alumno:
        print("dni del alumno: ", dni)
        print("materias que cursa y notas: ")
        for nota, materia in alumno[dni]:
            print(materia, nota)

def consulta(alumno):
    dni = int(input("ingrese su dni para consultar: "))
    if dni in alumno:
        for nota, materia in alumno[dni]:
            print(nota, materia)


#bloque main

alumno = carga()
listar(alumno)
consulta(alumno)
