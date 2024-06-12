def solicitarDatos():
   print("\n")
#    global n1,n2
   n1=int(input("Numero #1: "))
   n2=int(input("Numero #2: "))
   return n1,n2

def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        return f"{num1} + {num2} = {int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        return f"{num1} - {num2} = {int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        return f"{num1} * {num2} = {int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        return f"{num1} / {num2} = {int(num1)/int(num2)}"      
    else:
        print("opcion invalida")

def esperatecla():
    print("Presiona cualquier tecla para continuar")
    input()

peliculas = []
def agregar(pelicula):
    peliculas.append(pelicula)
    print(f"\nLa pelicula {pelicula} se agrego correctamente\n")
    print(peliculas)
    return peliculas

def eliminar(pelicula):
    peliculas.remove(pelicula)
    print(f"\nLa pelicula {pelicula} se elimino correctamente\n")
    print(peliculas)
    return peliculas

def consultar(pelicula):
    if pelicula in peliculas:
        print(f"\nLa pelicula {pelicula} se encuentra en la lista\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    return peliculas

def menu():
    print("\n1.- Agregar pelicula\n2.- Eliminar pelicula\n3.- Consultar pelicula\n4.- Salir\n")
    opcion = int(input("\tIngresa una opcion: "))
    return opcion
