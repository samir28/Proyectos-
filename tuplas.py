#bloque principal

#declara la tupla
fecha_tupla1 = (25, 12, 2016)
print("imprimos la primer tupla")
print(fecha_tupla1)
#conversion de tupla a lista
fecha_lista = list(fecha_tupla1)
print("imprimimos la lista que se le copio la tupla")
print(fecha_lista)
#agrego un valor a la lista en la posicion 0
fecha_lista[0] = 31
print("imprimimos la lista ya modificada")
print(fecha_lista)
#declaro otra tupla
fecha_tupla2 = tuple(fecha_lista)
print("imprimimos la segunda tupla que se copio a la lista")
print(fecha_tupla2)


