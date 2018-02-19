def carga():
    persona = {}
    for x in range(4):
        numero = int(input("ingrese el dni: "))
        nombre = input("ingrese el nombre: ")
        persona[numero] = nombre
    return persona


def imprimir(persona):
    print("listado del diccionario completo")
    for numero in persona:
        print(numero, persona[numero])



def consulta_por_num(persona):
    nu = int(input("ingrese el numero de documento a consultar: "))
    if nu in persona:
        print("nombre de la persona: ", persona[nu])
    else:
        print("no existe una persona con dicho numero de documento")

#bloque principal

persona = carga()
imprimir(persona)
consulta_por_num(persona)
