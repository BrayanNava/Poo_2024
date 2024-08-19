from conexionBD import *

class Revision ():
        def __init__(self,no_revision,matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros):
            self.cambiodefiltro = cambiodefiltro
            self.cambioaceite = cambioaceite
            self.cambiofrenos = cambiofrenos
            self.otros = otros

def insertar_revision(no_revision,matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros):
    try:
        cursor.execute(
            "INSERT INTO Revisiones (matricula, otro) VALUES (%s, %s)",
            (matricula, otro)
        )
        connection.commit()
        print("Revisión insertada correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar revisión: {err}")

def consultar_revision(no_revision):
    try:
        cursor.execute("SELECT * FROM Revisiones WHERE no_revision = %s", (no_revision,))
        revision = cursor.fetchone()
        return revision
    except mysql.connector.Error as err:
        print(f"Error al consultar revisión: {err}")

def actualizar_revision(no_revision,matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros):
    try:
        cursor.execute(
            "UPDATE Revisiones SET matricula=%s, cambiodefiltro=%s, cambioaceite=%s, cambioaceite=%s, otros=%s WHERE no_revision=%s",
            (matricula,cambiodefiltro,cambioaceite,cambiofrenos,otros)
        )
        connection.commit()
        print("Revisión actualizada correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar revisión: {err}")

def eliminar_revision(no_revision):
    try:
        cursor.execute("DELETE FROM Revisiones WHERE no_revision=%s", (no_revision,))
        connection.commit()
        print("Revisión eliminada correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar revisión: {err}")