def carga():
    empleado = []
    for x in range(5):
        nombre = input("nombre del empleado: ")
        sueldos = int(input("ingrese su sueldo: "))
        empleado.append((nombre, sueldos))
    return empleado

def imprimir(empleado):
    print("listado de los nombres de empleados y sueldos: ")
    for nombre, sueldos in empleado:
        print(nombre, sueldos)

def mayor_sueldo(empleado):
    empleado = empleado[0]
    for em in empleado:
        if em[1] > empleado[1]:
            print("empleado con mayor sueldo: ", em)

def menor_sueldo(empleado):
    cant = 0
    for emp in empleado:
        if empleado[1] < 1000:
            cant = cant + 1
        print("la cantidad de empleados con un sueldo menor a 1000 son: ", cant) 

#bloque de main

empleado = carga()
imprimir(empleado)
mayor_sueldo(empleado)
menor_sueldo(empleado)

