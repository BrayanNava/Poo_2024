# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir el contenido de la lista en mayusculas

palabras = []

if not palabras:
    print("La lista está vacía. Puedes agregar palabras o frases.")

while True:
    entrada = input("Introduce una palabra o frase (o escribe 'salir' para detenerte): ")
    if entrada.lower() == 'salir':
        break
    palabras.append(entrada)

print("\nContenido de la lista en mayúsculas:")
for palabra in palabras:
    print(palabra.upper())
