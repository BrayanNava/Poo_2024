# Lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una funcion lambda para fltrar los numeros pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimimos el resultado
print(numeros_pares)