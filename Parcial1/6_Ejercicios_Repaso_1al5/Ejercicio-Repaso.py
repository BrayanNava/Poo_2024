#crear un programa que calcule y obtenga el total a pagar por un producto determinado. sedevera de solicitar el nombre y descripcion del pructo, codigo del prodicto cantidad del producto precio unitario del producto.
# El total a pagar incluye el iva y el descuento.
# Si se compran de 1 a 5 producto se otorga el 10% de decuenti, si son de 6 a 10 el 15 % de descuento y si se compran mas de 10 el 20% de descuento, el iva es el 16%

nombre=input("Ingrese el nombre del producto: ")
codigo=int(input("Ingrese el codigo del producto: "))
cantidad=int(input("Ingrese la cantidad del producto: "))
precio=float(input("Ingrese el precio unitario del producto: "))

total=cantidad*precio

if cantidad>=1 and cantidad<=5:
    descuento=total*0.1
    total=total-descuento
    iva=total*0.16
    total=total+iva
    print(f"El total a pagar es: {total}")
elif cantidad>=6 and cantidad<=10:
    descuento=total*0.15
    total=total-descuento
    iva=total*0.16
    total=total+iva
    print(f"El total a pagar es: {total}")
elif cantidad>10:
        descuento=total*0.2
        total=total-descuento
        iva=total*0.16
        total=total+iva


print(f"El total a pagar es: {total}")
