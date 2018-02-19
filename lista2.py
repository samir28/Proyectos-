lista = []

for x in range(10):
    valor = int(input("ingresar un valor: "))
    lista.append(valor)

print("la lista de valores")
print(lista)

pos = 0
while pos < len(lista):
    if lista[pos] == 5:
        lista.pop(pos)
    else:
        pos = pos + 1

print("la lista de valores sin el 5")
print(lista)
