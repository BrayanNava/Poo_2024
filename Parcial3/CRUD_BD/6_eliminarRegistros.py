from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="delete from clintes where id=3"
    micursor.execute(sql)

    conexion.commit()
except:
    print("Occurio un Error Por Favor Verifica...")
else:
    print("Registro eliminado Exitosamente")