# 4.- 

# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico, y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = [1, 2, 3]
cadena = "Hola, Marshal"
entero = 302
logico = True

def tipo(variable):
    if isinstance(variable, list):
        print(f"La variable es una lista: {variable}")
    elif isinstance(variable, str):
        print(f"La variable es una cadena: '{variable}'")
    elif isinstance(variable, int):
        print(f"La variable es un entero: {variable}")
    elif isinstance(variable, bool):
        print(f"La variable es un lógico: {variable}")


tipo(lista)

tipo(cadena)

tipo(entero)

tipo(logico)