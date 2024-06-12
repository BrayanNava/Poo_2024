# Ejemplo 5 Crear un programa que permita gestionar (administrar) peliculas, clocar un menu de opcione para agregar, remover, consultar peliculas.
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas

from varias_funciones import *

peliculas = []

def agregar(pelicula):
    peliculas.append(pelicula)
    print(f"\nLa pelicula {pelicula} se agregó correctamente\n")
    print(peliculas)
    return peliculas

def eliminar(pelicula):
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"\nLa pelicula {pelicula} se eliminó correctamente\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    print(peliculas)
    return peliculas

def consultar(pelicula):
    if pelicula in peliculas:
        print(f"\nLa pelicula {pelicula} se encuentra en la lista\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    return peliculas

def actualizar(pelicula, nueva_pelicula):
    if pelicula in peliculas:
        indice = peliculas.index(pelicula)
        peliculas[indice] = nueva_pelicula
        print(f"\nLa pelicula {pelicula} se actualizó correctamente a {nueva_pelicula}\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    print(peliculas)
    return peliculas

def buscar(pelicula):
    if pelicula in peliculas:
        print(f"\nLa pelicula {pelicula} se encuentra en la lista\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    return peliculas

def vaciar():
    peliculas.clear()
    print("\nLa lista de peliculas se ha vaciado correctamente\n")
    return peliculas

def menu():
    print("\n1.- Agregar\n2.- Eliminar\n3.- Consultar\n4.- Actualizar\n5.- Buscar\n6.- Vaciar\n7.- Salir\n")
    opcion = int(input("\tIngresa una opción: "))
    return opcion

opcion = menu()

while opcion != 7:
    if opcion == 1:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        agregar(pelicula)
    elif opcion == 2:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        eliminar(pelicula)
    elif opcion == 3:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        consultar(pelicula)
    elif opcion == 4:
        pelicula = input("\nIngresa el nombre de la pelicula a actualizar: \n")
        nueva_pelicula = input("\nIngresa el nuevo nombre de la pelicula: \n")
        actualizar(pelicula, nueva_pelicula)
    elif opcion == 5:
        pelicula = input("\nIngresa el nombre de la pelicula a buscar: \n")
        buscar(pelicula)
    elif opcion == 6:
        vaciar()
    elif opcion < 1 or opcion > 7:
        print("\nOpcion no valida")
    opcion = menu()

print("\nGracias por usar el programa")
