# Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados=0
reprobados=0
for i in range(1,16):
    i=int(input("Ingrese la calificacion: "))
    if i>=80:
        aprobados+=1
        print("Aprobado")
    else:
        reprobados+=1
        print("Reprobado")

print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
