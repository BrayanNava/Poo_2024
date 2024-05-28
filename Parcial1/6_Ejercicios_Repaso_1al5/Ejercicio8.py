# Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


x = float(input("Ingrese un numero: "))
porcentaje = float(input("Ingrese un porcentaje: "))
resultado = int(x * (porcentaje / 100))
print(f"El resultado es: {resultado}")
