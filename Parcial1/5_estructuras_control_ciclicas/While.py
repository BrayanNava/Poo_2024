# el siclo while es una estructura de control que itera o repite la ejecucion de una serie de instrucciones tantas veses como la condicion se cumpla 'true'

# sintaxis:
# while condicion
#     bloque de instrucciones

# ejemplo 1 Crear un programa que imprima 5 vesex el caracter @

contador=1
while contador <=5:
    print("@")
    contador+=1

#Ejemplo 2 Crear un programa que imprim los numeros del 1 al 5 los sume y alfanl imprima la suma

contador=1
suma=0
while contador <=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es : {suma}")

#Ejemplo 3 Crear un programa que solicite un numero entre e continuacion imprima la tabla de multiplicar correspondiente

numero=int(input("Ingresa un numero: "))

multi=0
i=1
while i<=10:
  multi=i*numero
  print(f"{numero} X {i} = {multi}")
i+=1
