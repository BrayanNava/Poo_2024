# Es un ciclo interativo y se ejecuta x veses deacuerdo a los balores numericos establesidos.

# sintaxis:
# for variable in elemento_interable:
#     Bloque de istrucciones

# ejemplo 1 Crear un programa que imprima 5 vesex el caracter @

for contador in range(1,6):
    print("@")


#Ejemplo 2 Crear un programa que imprim los numeros del 1 al 5 los sume y alfanl imprima la suma
suma=0
for numero in range (1,6):
    print(numero)
    suma+=numero
print(f"La suma es :{suma}")

#Ejemplo 3 Crear un programa que solicite un numero entre e continuacion imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero: "))
for i in range (1,11):
    print(f"{numero} x {i} = {numero*i}")