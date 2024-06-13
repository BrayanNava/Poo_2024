pregunta = "SI"

while pregunta == "SI":
    nombre = input("Ingresa el Nombre del Alumno: ")
    carrera = input("Ingrese la Carrera: ")
    calificacion1 = int(input("Ingrese la calificacion de la primera unidad: "))
    calificacion2 = int(input("Ingrese la calificacion de la segunda unidad: "))
    calificacion3 = int(input("Ingrese la calificacion de la tercera unidad: "))
    proyecto = int(input("Ingrese la calificacion del proyecto final: "))

    promedio_parcial = ((calificacion1 + calificacion2 + calificacion3) / 3)
    calificacion_final = ((promedio_parcial + proyecto) / 2)

    print(f"El promedio del parcial es {promedio_parcial}")
    print(f"La calificacion final es {calificacion_final}")

    if calificacion_final < 80 and proyecto > 50:
        print("Presentar Examen Extraordinario")
    else:
        print(f"El alumno {nombre} Aprobado")

    pregunta = input("¿Desea otra captura? (SI/NO): ").upper()
    while pregunta not in ["SI", "NO"]:
        pregunta = input("¿Desea otra captura? (SI/NO): ").upper()

print("¡Hasta luego!")
