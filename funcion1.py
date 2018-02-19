def promedio(v1, v2, v3):
    suma = v1 + v2 + v3
    promedio = suma // 3
    return promedio

#bloque principal

n1 = int(input("ingrese un valor: "))
n2 = int(input("ingrese un valor: "))
n3 = int(input("ingrese un valor: "))

print("el promedio es: ", promedio(n1, n2, n3))


