empleado = []
sueldo = []

cant = int(input("cuantos empleados hay: "))
for x in range(cant):
    nombre = input("ingrese el nombre: ")
    empleado.append(nombre)
    sue = int(input("ingrese el sueldo: "))
    sueldo.append(sue)

print("listado completo de empleados: ")
for x in range(len(sueldo)):
    print(empleado[x], sueldo[x])

pos = 0
while pos < len(sueldo):
    if sueldo[pos] > 10000:
        sueldo.pop(pos)
        empleado.pop(pos)
    else:
        pos = pos + 1
print("listado de empleado que cobran 10000 o menos: ")
for x in range(len(sueldo)):
    print(empleado[x], sueldo[x])


