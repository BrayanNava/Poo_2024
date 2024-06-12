# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud sea menor a 120, y luego mostrar la lista: Usar un while y for

numeros = []

while len(numeros) <= 120:
    entrada = input(f"Introduce un número (actual: {len(numeros)} elementos, máximo 120): ")
    numeros.append(entrada)

print("Lista completa:")
for numero in numeros:
    print(str(numero))
