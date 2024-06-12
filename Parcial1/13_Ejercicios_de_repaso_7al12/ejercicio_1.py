# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

numeros = [20, 8, 27, 42, 15, 32, 1, 42]

print("La lista:")
for numero in numeros:
    print(numero)

def lista_string(lista):
    return ", ".join(str(numero) for numero in lista)

resultado = lista_string(numeros)
print("Lista en string:")
print(resultado)

numeros_ordenados = sorted(numeros)
print("Lista ordenada:")
for numero in numeros_ordenados:
    print(numero)

longitud = len(numeros)
print("Longitud de la lista:")
print(longitud)

buscar = int(input("Introduce un número para buscar en la lista: "))

if buscar in numeros:
    print(f"El número {buscar} se encuentra en la lista.")
else:
    print(f"El número {buscar} no se encuentra en la lista.")
