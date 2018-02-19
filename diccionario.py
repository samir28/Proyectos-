def carga():
    diccionario = {}
    continua = "s"
    while continua == "s":
        cast = input("ingrese palabra en castellano: ")
        ing = input("ingrese palabra en ingles: ")
        diccionario[ing] = cast
        continua = input("quiere cargar otra palabra: [s/n]")
    return diccionario

def imprimir(diccionario):
    print("listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def consulta_palabra(diccionario):
    pal = input("ingrese la palabra en ingles a consultar: ")
    if pal in diccionario:
        print("en castellano significa: ", diccionario[pal])

    




#bloque principal

diccionario = carga()
imprimir(diccionario)
consulta_palabra(diccionario)


