"""cuando se imprime en pantalla una cadena de caracteres 
se trabaja por default con "cadenas" es decir python no 
puede concatenar otra cosa que no sea un strinf(str) """

texto="Soy una cadena de caracteres"
numero=23

#Concatenar str con str
print("Soy otra cadena y " +texto)

#Concatenar str con int

numero_str=str(numero)
print("El numero: "+numero_str)
print("El numero: "+str(numero))

##concatenar int con str

n1=int('23')
n2=33

suma=n1+n2
print(f"la suma es: {suma}")

# concatenar float y int cons str

n1=23.99
n2=33.0

suma=int(n1+n2)
print(f"la suma es: {suma}")
