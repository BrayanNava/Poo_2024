#los errores de excepciones en un leguaje de programacion no es otra cosas que los errores en tiempo de ejecucion entonses cunado se manejan los errores mediante la excepciones en realidad se dice que se evita que se precenten esos errores en el programa en tiempo de ejecucion :)

#ejemplo se precenta un error cuando no es jenerada una vareable 

try:
    nombre=input("Dame el nombre completo de una persoa: ")

    if len(nombre)>0:
        nombre_usuario = "El nombre del usuari del sistema es: "+nombre

    print(nombre_usuario)
except:
    print("Es nesesario el nombre de una persona")

#Ejemplo 2 cuando se solisita un numero y se ingresa otra cosa

try:
    numero=int(input("ingresa un numero entero: "))

    if numero > 0:
        print("Soy un numero entero positivo")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print("No es posible una letra a un numero, verific por favor")

#Ejemplo 3 Cuando se generan multiples exepciones

try:
    numero=int(input("ingresa un numero"))

    print("El cuadrado del numero es: "+str(numero*numero))
except TypeError:
    print("debes de combertir el numero a entreo")
except ValueError:
    print("No es posible una letra a un numero, verific por favor")
else:
    print("No se genero ningun error")
finally:
    print("ya termino")
