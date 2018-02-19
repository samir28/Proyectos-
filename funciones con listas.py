def sumar_lista(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

def mayor_lista(lista):
    may = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may

def menor_lista(lista):
    men = lista[0]
    for x in range(1,len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men

#bloque principal

lista_valores = [10, 56, 23, 120, 94]
print("la lista completa es: ")
print(lista_valores)
print("la suma de todos los valores es: ", sumar_lista(lista_valores))
print("el mayor elemento de la lista es: ", mayor_lista(lista_valores))
print("el menor elemento de la lista es: ", menor_lista(lista_valores))

