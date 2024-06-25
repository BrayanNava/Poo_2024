
from Coches import *

# print("Objeto 1")
coche1=Coches("Banco","2022","VW",220,150,5)
# coche1.getInfo()


# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,150,6)
# coche2.getInfo()

print(coche1.publico_atrubuto)
#print(coche1.privado_atrubuto) esto no es permitido
print(coche1.getPrivadoAtrivuto())

# coche1.__getMetodoPrivado() esto no es permitido
coche1.getMetodoPublico()