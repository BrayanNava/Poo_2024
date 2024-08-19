from conexionBD import *

class Cliente:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        pass

def insertar_cliente(nif, nombre, direccion, ciudad, tel):
    try:
        cursor.execute(
            "INSERT INTO Clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)",
            (nif, nombre, direccion, ciudad, tel)
        )
        conexion.commit()
        print("Cliente insertado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar cliente: {err}")
        conexion.rollback()


def consultar_clientes():
    try:
        cursor.execute("SELECT * FROM Clientes")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error al consultar clientes: {err}")
        return []

def actualizar_cliente(nif, nombre, direccion, ciudad, tel):
        cursor.execute("UPDATE Clientes SET nombre=%s, direccion=%s, ciudad=%s, tel=%s WHERE nif=%s",
                       (nombre, direccion, ciudad, tel, nif))
        conexion.commit()

def eliminar_cliente(nif):
    try:
        cursor.execute("DELETE FROM Clientes WHERE nif=%s", (nif,))
        conexion.commit()
        print("Cliente eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar cliente: {err}")
        conexion.rollback()