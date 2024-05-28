# Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario


inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

print("Números entre", inicio, "y", fin, ":")

if inicio > fin:
    inicio, fin = fin, inicio

for numero in range(inicio, fin + 1):
    print(numero, end=" ")