import clientes 
import autos
import revisiones
from funciones import *

def menu():
    while True:
        borrarPantalla()
        print("\n--- Menú Principal ---")
        print("1. Clientes")
        print("2. Autos")
        print("3. Revisiones")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            menu_clientes()
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            menu_autos()
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            menu_revisiones()
            esperarTecla()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

def menu_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nif = int(input("NIF: "))
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            tel = int(input("Teléfono: "))
            clientes.insertar_cliente(nif, nombre, direccion, ciudad, tel)
            print("Cliente insertado con éxito.")
        elif opcion == '2':
            clientes_lista = clientes.consultar_clientes()
            for cliente in clientes_lista:
                print(cliente)
        elif opcion == '3':
            nif = int(input("NIF del cliente a actualizar: "))
            nombre = input("Nuevo Nombre: ")
            direccion = input("Nueva Dirección: ")
            ciudad = input("Nueva Ciudad: ")
            tel = int(input("Nuevo Teléfono: "))
            clientes.actualizar_cliente(nif, nombre, direccion, ciudad, tel)
            print("Cliente actualizado con éxito.")
        elif opcion == '4':
            nif = int(input("NIF del cliente a eliminar: "))
            clientes.eliminar_cliente(nif)
            print("Cliente eliminado con éxito.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

def menu_autos():
    while True:
        print("\n--- Gestión de Autos ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = int(input("Modelo: "))
            color = input("Color: ")
            nif = int(input("NIF del propietario: "))
            autos.insertar_auto(matricula, marca, modelo, color, nif)
            print("Auto insertado con éxito.")
        elif opcion == '2':
            autos_lista = autos.consultar_autos()
            for auto in autos_lista:
                print(auto)
        elif opcion == '3':
            matricula = input("Matrícula del auto a actualizar: ")
            marca = input("Nueva Marca: ")
            modelo = int(input("Nuevo Modelo: "))
            color = input("Nuevo Color: ")
            nif = int(input("Nuevo NIF del propietario: "))
            autos.actualizar_auto(matricula, marca, modelo, color, nif)
        elif opcion == '4':
            matricula = input("Matrícula del auto a eliminar: ")
            autos.eliminar_auto(matricula)
            print("Auto eliminado con éxito.")

def menu_revisiones():
    while True:
        print("\n--- Gestión de Revisiones ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            matricula = input("Matrícula del auto: ")
            cambiodefiltro = input("Cambiodefiltro? (Y/N) ")
            cambioaceite = input("Cambioaceite? (Y/N) ")
            cambiofrenos = input("Cambiofrenos? (Y/N) ")
            otros = input("si no es esta de enter:  ")
            revisiones.insertar_revision(matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros)

        elif opcion == '2':
            no_revision = input("Número de la revisión: ")
            revision = revisiones.consultar_revision(no_revision)
            if revision:
                print(f"No. Revisión: {revision[0]}")
                print(f"Matrícula: {revision[1]}")
                print(f"Fecha: {revision[2]}")
                print(f"Descripción: {revision[3]}")
            else:
                print("Revisión no encontrada.")

        elif opcion == '3':
            no_revision = input("Número de la revisión: ")
            cambiodefiltro = input("Cambiodefiltro? (Y/N) ")
            cambioaceite = input("Cambioaceite? (Y/N) ")
            cambiofrenos = input("Cambiofrenos? (Y/N) ")
            otros = input("si no es esta de enter:  ")
            revisiones.actualizar_revision(no_revision,matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros)

        elif opcion == '4':
            no_revision = input("Número de la revisión a eliminar: ")
            revisiones.eliminar_revision(no_revision)

        elif opcion == '5':
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()