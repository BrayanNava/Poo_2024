#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = int(numero1 + numero2)
resta = int(numero1 - numero2)
multiplicacion = int(numero1 * numero2)

if numero2 != 0:
    division = int(numero1 / numero2)
else:
    division = "No se puede dividir por cero"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)