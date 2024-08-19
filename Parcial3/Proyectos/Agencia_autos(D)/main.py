from db import * 
from modelos import *
from funciones import * 

def menu():
    while True:
        print("\tA.::: Agencia de Autos :::.\n1. Autos\n2. Revisiones\n3. Clientes\n4. Salir")
        opc = int(input("Selecciona una opcion: "))
        borrarPantalla()
        
        if opc == 1:
            while1 = True
            while while1:
                borrarPantalla
                print("\t.::: Autos :::.\n1. Ingresar\n2. Modificar\n3. Eliminar\n4. Listar\n5. Salir")
                opcion = int(input("Selecciona una opcion: "))
                borrarPantalla()
            
                if opcion == 1:
                    auto = Autos(None, None, None, None, None)
                    auto.agregar_auto(cursor, conexion)
                    esperarTecla()
                
                if opcion == 2:
                    auto = Autos(None, None, None, None, None)
                    auto.modificar_auto(cursor, conexion)
                    esperarTecla()
                
                if opcion == 3:
                    auto = Autos(None, None, None, None, None)
                    auto.eliminar_auto(cursor, conexion)
                    esperarTecla()
                
                if opcion == 4:
                    auto = Autos(None, None, None, None, None)
                    auto.listar_autos(cursor, conexion)
                    esperarTecla()
                    
                if opcion == 5:
                    while1 = False
            
        if opc == 2:
            while2 = True
            while while2:
                borrarPantalla()
                print("\t.::: REVISIONES :::.\n1. Ingresar\n2. Modificar\n3. Eliminar\n4. Listar\n5. Salir")
                opcion = int(input("Selecciona una opcion: "))
                borrarPantalla()
                if opcion == 1:
                    revision = Revisiones(None, None, None, None, None, None)
                    revision.agregar_revision(cursor, conexion)
                    print("Revision registrada exitosamente.")
                    esperarTecla()
                    borrarPantalla()
                    
                elif opcion == 2:
                    revision = Revisiones(None, None, None, None, None, None)
                    revision.modificar_revision(cursor, conexion)
                    print("Revision modificada.")
                    esperarTecla()
                    borrarPantalla()
                    
                elif opcion == 3:
                    revision = Revisiones(None, None, None, None, None, None)
                    revision.eliminar_revision(cursor, conexion)
                    print("Revision eliminada exitosamente.")
                    esperarTecla()
                    borrarPantalla()
                    
                elif opcion == 4:
                    revision = Revisiones(None, None, None, None, None, None)
                    revision.listar_revisiones(cursor)
                    esperarTecla()
                    borrarPantalla()
                    
                elif opcion == 5:
                    print("Saliendo...")
                    while2 = False
        
        elif opc == 3:
            while3 = True
            while while3:
                print(".::: Clientes :::.\n1. Ingresar\n2. Modificar\n3. Eliminar\n4. Listar\n5. Salir")
            opcion = int(input("Selecciona una opcion: "))
            borrarPantalla()
            
            if opcion == 1:
                cliente = Clientes(None, None, None, None, None)
                cliente.agregar_cliente(cursor, conexion)
                esperarTecla()
                borrarPantalla()
                
            elif opcion == 2:
                cliente = Clientes(None, None, None, None, None)
                cliente.modificar_cliente(cursor, conexion)
                esperarTecla()
                borrarPantalla()
                
            elif opcion == 3:
                cliente = Clientes(None, None, None, None, None)
                cliente.eliminar_cliente(cursor, conexion)
                esperarTecla()
                borrarPantalla()
                
            elif opcion == 4:
                cliente = Clientes(None, None, None, None, None)
                cliente.listar_clientes(cursor, conexion)
                esperarTecla()
                borrarPantalla()
                
            elif opcion == 5:
                while3
                
        elif opc == 4:
            print("Saliendo...")
            break
        
menu()
    