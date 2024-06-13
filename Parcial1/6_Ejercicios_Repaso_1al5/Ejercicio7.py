# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

for inicio in range (inicio, fin):
    if inicio % 2!= 0:
        print(inicio)
