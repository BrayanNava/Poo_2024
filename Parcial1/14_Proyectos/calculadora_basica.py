import os
import math
from varias_funciones import *

def solicitarDatos():
    print("\n")
    global n1, n2
    n1 = int(input("Numero #1: "))
    n2 = int(input("Numero #2: "))

def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = f"{num1} + {num2} = {int(num1) + int(num2)}"
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        resultado = f"{num1} - {num2} = {int(num1) - int(num2)}"
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = f"{num1} * {num2} = {int(num1) * int(num2)}"
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = f"{num1} / {num2} = {int(num1) / int(num2)}"
    elif operacion == "5" or operacion == "POTENCIAR":
        resultado = f"{num1} ^ {num2} = {math.pow(num1, num2)}"
    elif operacion == "6" or operacion == "RAIZ":
        resultado = f"Raíz cuadrada de {num1} = {math.sqrt(num1)}"
    return resultado

def esperatecla():
    print("Presiona cualquier tecla para continuar")
    input()

opcion = True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potenciar \n 6.- Raíz \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion != "7":
        if opcion in ["1", "2", "3", "4",]:
            n1, n2 = solicitarDatos()
            print(getCalculadora(n1, n2, opcion))
        elif opcion in ["5"]:
            n1 = int(input("Ingrese el número: "))
            n2 = int(input("Ingrese el exponente: "))
            print(getCalculadora(n1, None, opcion))
            esperatecla()
        elif opcion in ["6"]:
            n1 = int(input("Ingrese el número: "))
            print(getCalculadora(n1, None, opcion))
        esperatecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema...")
