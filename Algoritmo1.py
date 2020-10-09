#algoritmo 1

A = int(input("Ingrese el número de la variable A: "))
B = int(input("Ingrese el número de la variable B: "))

Cambio = A
A = B
B = Cambio

print("EL contenido de la varialbes ha cambiado... \n")
print("El valor de la variable A ahora es: " + str(A) + " Y el valor de la variable B ahora es: " + str(B))
