import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='agencia_autos'
    )
    cursor=conexion.cursor()
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    
