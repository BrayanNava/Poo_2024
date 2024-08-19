import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_empleados'
    )
    cursor = conexion.cursor(buffered=True)
except:
    print(f"Ocurrió un error con el Sistema, por favor verifique ...")
