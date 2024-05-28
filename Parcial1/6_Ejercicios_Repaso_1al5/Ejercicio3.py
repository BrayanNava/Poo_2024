# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

# Usando for
for numero in range(1, 61):
    cuadrado = numero ** 2
    print(numero, "*", numero, "=", cuadrado)

# Usando while

numero = 1
while numero <= 60:
    cuadrado = numero ** 2
    print(numero, "*", numero, "=", cuadrado)
    numero = numero + 1
    