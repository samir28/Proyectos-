def carga_lista():
    li = []
    for x in range(5):
        valor = int(input("ingrese un valor: "))
        li.append(valor)
    return li

def retorna_mayor_menor(li):
    ma = li[0]
    me = li[0]
    for x in range(1,len(li)):
        if li[x] > ma:
            ma = li[x]
        else:
            if li[x] < me:
                me = li[x]
    return [ma, me]

#bloque principal

lista = carga_lista()
rango = retorna_mayor_menor(lista)
print("el mayor elemento de la lista es: ", rango[0])
print("el menor elemento de la lista es: ", rango[1])

    
