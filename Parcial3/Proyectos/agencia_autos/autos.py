from conexionBD import *

class Autos ():
    def __init__(self,matricula,marca,modelo,color):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def insertar(self):
        pass

def insertar_auto(matricula, marca, modelo, color, nif):
    try:
        cursor.execute(
            "INSERT INTO Autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)",
            (matricula, marca, modelo, color, nif)
        )
        conexion.commit()
        print("Cliente insertado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar auto: {err}")
        conexion.rollback()

def consultar_autos():
    try:
        cursor.execute("SELECT * FROM Autos")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error al consultar Auto: {err}")
        return []

def actualizar_auto(matricula, marca, modelo, color, nif):
    try:
        cursor.execute(
            "UPDATE Autos SET nif=%s, marca=%s, modelo=%s, color=%s WHERE matricula=%s",
            (nif, marca, modelo, color, matricula)
        )
        conexion.commit()
        print("Auto actualizado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar auto: {err}")

def eliminar_auto(matricula):
    try:
        cursor.execute("DELETE FROM Autos WHERE matricula=%s", (matricula,))
        conexion.commit()
        print("Auto eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar Auto: {err}")
        conexion.rollback()