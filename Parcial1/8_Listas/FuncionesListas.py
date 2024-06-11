
paises=["Mexico","E.U.A","Brasil","Japoon"]
numero=[23,34,12.56,0.100,23]
texto=["Hola",True,23,3.1426]

# ordenar una lista

# print(paises)
# paises.sort()
# print(paises)

# print(numero)
# numero.sort()
# print(numero)

# #Añadir elemontos
# print(texto)
# texto.insert(len(texto),"True")
# print(texto)
# texto.insert(len(texto),True)
# print(texto)
# texto.append(False)
# print(texto)

# #eliminar elemntos

# print(numero)
# numero.remove(23)
# print(numero)
# numero.pop(0)
# print(numero)

#dar la vuelta

print(numero)
numero.reverse()
print(numero)

#buscar Datos dentro de una lista

respuesta="Brasil" in paises
print(respuesta)

#cuantasvese aparece un valor dentro de una lista

print(numero)
numero.append(23)
cuantos=numero.count(23)
print(f"El numero 23 se encontro: {cuantos}")

#Unir listas

print(paises)
paises.extend(numero)
print(paises)

print(numero)
numero.sort()
print(numero)
