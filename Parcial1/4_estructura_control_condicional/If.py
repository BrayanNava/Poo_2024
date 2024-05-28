""" 
    Existe una estructura de condicion llamada "If" la cual evalua una condicion para encontrar el valor "True" o se cumple la condicion se ejecutar la linea o las lineas de codigo

    tienes 4 tipos de If
    1.-El if simple
    2.-El if compuesto
    3.-El if anidado
    4.-El if y elif
"""
#Ejemplo 1 If simple

color=rojo

if color=="rojo":
    Print("Soy el color rojo")

#Ejemplo 2 If compuesto

color=rojo

if color=="rojo":
    Print("Soy el color rojo")
else:
    Print("No soy el color rojo")

#Ejemplo 3 If anidado

color=rojo

if color=="rojo":
    Print("Soy el color rojo")
    if color!="rojo":
        Print("Soy otro color")

#Ejemplo 4 If y elif

color=rojo

if color=="rojo":
    Print("Soy el color rojo")
elif color=="negro":
    Print("Soy negro")
elif color=="verde":
    Print("Soy el color verde")
else:
    Print("No soy ningun color")
    