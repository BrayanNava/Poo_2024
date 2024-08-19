from db import *

from db import *

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
        
    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getNif(self):
        return self.nif
    def setNif(self, nif):
        self.nif = nif

    def agregar_auto(self, cursor, conexion):
        try:
            # Captura de datos
            self.matricula = input("Matrícula del Auto: ")
            self.marca = input("Marca del Auto: ")
            self.modelo = int(input("Modelo del Auto (Año): "))
            self.color = input("Color del Auto: ")
            self.nif = int(input("NIF del Cliente: "))

            cursor.execute('''
                INSERT INTO autos (matricula, marca, modelo, color, nif)
                VALUES (%s, %s, %s, %s, %s)
            ''', (self.matricula, self.marca, self.modelo, self.color, self.nif))

            conexion.commit()

            print("Auto agregado exitosamente con Matrícula:", self.matricula)
        except:
            print("No hay un cliente con el NIF, Registralo antes de introducir un Auto.")

    def modificar_auto(self, cursor, conexion):
        while True:
            cursor.execute("SELECT * FROM autos")
            autos = cursor.fetchall()
            
            print("Listado de Autos:")
            for auto in autos:
                print(f"Matrícula: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}, Color: {auto[3]}, NIF: {auto[4]}")
            
            opcion = input("Seleccione la matrícula del auto que desea modificar o elija una opción: ")
            
            if len(opcion) == 7:  # La matrícula tiene 7 caracteres
                matricula = opcion
                cursor.execute("SELECT * FROM autos WHERE matricula = %s", (matricula,))
                auto = cursor.fetchone()
                
                if auto:
                    self.matricula = auto[0]
                    self.marca = auto[1]
                    self.modelo = auto[2]
                    self.color = auto[3]
                    self.nif = auto[4]
                    
                    while True:
                        print("Modificar datos del auto:")
                        print("1. Marca")
                        print("2. Modelo")
                        print("3. Color")
                        print("4. NIF")
                        print("5. Todos")
                        print("6. Cancelar")

                        modificacion = input("Elija la opción a modificar: ")

                        if modificacion == "1":
                            nueva_marca = input("Nueva Marca: ")
                            cursor.execute("UPDATE autos SET marca = %s WHERE matricula = %s", (nueva_marca, self.matricula))
                            self.marca = nueva_marca
                        elif modificacion == "2":
                            nuevo_modelo = int(input("Nuevo Modelo (Año): "))
                            cursor.execute("UPDATE autos SET modelo = %s WHERE matricula = %s", (nuevo_modelo, self.matricula))
                            self.modelo = nuevo_modelo
                        elif modificacion == "3":
                            nuevo_color = input("Nuevo Color: ")
                            cursor.execute("UPDATE autos SET color = %s WHERE matricula = %s", (nuevo_color, self.matricula))
                            self.color = nuevo_color
                        elif modificacion == "4":
                            nuevo_nif = int(input("Nuevo NIF: "))
                            cursor.execute("UPDATE autos SET nif = %s WHERE matricula = %s", (nuevo_nif, self.matricula))
                            self.nif = nuevo_nif
                        elif modificacion == "5":
                            nueva_marca = input("Nueva Marca: ")
                            nuevo_modelo = int(input("Nuevo Modelo (Año): "))
                            nuevo_color = input("Nuevo Color: ")
                            nuevo_nif = int(input("Nuevo NIF: "))

                            cursor.execute('''
                                UPDATE autos
                                SET marca = %s, modelo = %s, color = %s, nif = %s
                                WHERE matricula = %s
                            ''', (nueva_marca, nuevo_modelo, nuevo_color, nuevo_nif, self.matricula))
                            
                            self.marca = nueva_marca
                            self.modelo = nuevo_modelo
                            self.color = nuevo_color
                            self.nif = nuevo_nif
                        elif modificacion == "6":
                            print("Modificación cancelada.")
                            break
                        else:
                            print("Opción no válida.")
                            continue

                        conexion.commit()
                        print("Datos actualizados correctamente.")
                        break
                else:
                    print("Auto no encontrado.")
            elif opcion == "0":
                print("Saliendo del menú de modificación.")
                break
            else:
                print("Opción no válida.")
                
    def eliminar_auto(self, cursor, conexion):
        while True:
            cursor.execute("SELECT * FROM autos")
            autos = cursor.fetchall()

            print("Listado de Autos:")
            for auto in autos:
                print(f"Matrícula: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}, Color: {auto[3]}, NIF: {auto[4]}")

            matricula = input("Ingrese la matrícula del auto que desea eliminar o '0' para cancelar: ")

            if len(matricula) == 7:  # La matrícula tiene 7 caracteres
                if matricula == '0':
                    print("Cancelando operación de eliminación.")
                    break

                cursor.execute("SELECT * FROM autos WHERE matricula = %s", (matricula,))
                auto = cursor.fetchone()

                if auto:
                    cursor.execute("DELETE FROM autos WHERE matricula = %s", (matricula,))
                    conexion.commit()
                    print(f"Auto con matrícula {matricula} eliminado correctamente.")
                    break
                else:
                    print("Auto no encontrado.")
            else:
                print("Matrícula no válida. Por favor, ingrese una matrícula válida.")

    @staticmethod
    def listar_autos(cursor, conexion):
        cursor.execute("SELECT * FROM autos")
        autos = cursor.fetchall()
            
        print("Listado de Autos:")
        for auto in autos:
            print(f"Matrícula: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}, Color: {auto[3]}, NIF: {auto[4]}")


class Revisiones():
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula
        
    def getNoRevision(self):
        return self.no_revision
    def setNoRevision(self, no_revision):
        self.no_revision = no_revision
        
    def getCambioFiltro(self):
        return self.cambiofiltro
    def setCambioFiltro(self, cambiofiltro):
        self.cambiofiltro = cambiofiltro

    def getCambioAceite(self):
        return self.cambioaceite
    def setCambioAceite(self, cambioaceite):
        self.cambioaceite = cambioaceite
        
    def getCambioFrenos(self):
        return self.cambiofrenos
    def setCambioFrenos(self, cambiofrenos):
        self.cambiofrenos = cambiofrenos

    def getOtros(self):
        return self.otros
    def setOtros(self, otros):
        self.otros = otros

    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula = matricula

    def agregar_revision(self, cursor, conexion):
        try:
            while True:
                # Captura de datos
                self.no_revision = int(input("Número de Revisión: "))
                self.cambiofiltro = input("Cambio de Filtro (S/N): ")
                self.cambioaceite = input("Cambio de Aceite (S/N): ")
                self.cambiofrenos = input("Cambio de Frenos (S/N): ")
                self.otros = input("Otros cambios: ")
                self.matricula = input("Matrícula del Auto: ")

                # Verificar si la matrícula del auto existe en la tabla autos
                cursor.execute("SELECT * FROM autos WHERE matricula = %s", (self.matricula,))
                auto = cursor.fetchone()

                if auto:
                    # Insertar los datos en la tabla revisiones
                    cursor.execute('''
                        INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    ''', (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula))

                    conexion.commit()

                    print("Revisión agregada exitosamente con Número de Revisión:", self.no_revision)
                    break
                else:
                    print("La matrícula del auto no existe. Por favor, ingrese una matrícula válida.")
                    continuar = input("¿Desea intentar nuevamente? (S/N): ")
                    if continuar.lower() != 's':
                        print("Operación cancelada.")
                        break
        except:
            print("No existe un auto con esa Matricula.")

        
    def modificar_revision(self, cursor, conexion):
            cursor.execute("SELECT * FROM revisiones")
            revisiones = cursor.fetchall()
            
            print("Listado de Revisiones:")
            for revision in revisiones:
                print(f"No. Revisión: {revision[0]}, Cambio de Filtro: {revision[1]}, Cambio de Aceite: {revision[2]}, Cambio de Frenos: {revision[3]}, Otros: {revision[4]}, Matrícula: {revision[5]}")
            
            opcion = input("Seleccione el número de revisión que desea modificar o presione 0 para cancelar: ")
            
            if opcion.isdigit():
                no_revision = int(opcion)
                cursor.execute("SELECT * FROM revisiones WHERE no_revision = %s", (no_revision,))
                revision = cursor.fetchone()
                
                if revision:
                    self.no_revision = revision[0]
                    self.cambiofiltro = revision[1]
                    self.cambioaceite = revision[2]
                    self.cambiofrenos = revision[3]
                    self.otros = revision[4]
                    self.matricula = revision[5]
                    
                    while True:
                        print("Modificar datos de la revisión:")
                        print("1. Cambio de Filtro")
                        print("2. Cambio de Aceite")
                        print("3. Cambio de Frenos")
                        print("4. Otros")
                        print("5. Matrícula")
                        print("6. Todos")
                        print("7. Cancelar")

                        modificacion = input("Elija la opción a modificar: ")

                        if modificacion == "1":
                            nuevo_cambiodfiltro = input("Nuevo Cambio de Filtro (S/N): ")
                            cursor.execute("UPDATE revisiones SET cambiofiltro = %s WHERE no_revision = %s", (nuevo_cambiodfiltro, self.no_revision))
                            self.cambiofiltro = nuevo_cambiodfiltro
                        elif modificacion == "2":
                            nuevo_cambiodaceite = input("Nuevo Cambio de Aceite (S/N): ")
                            cursor.execute("UPDATE revisiones SET cambioaceite = %s WHERE no_revision = %s", (nuevo_cambiodaceite, self.no_revision))
                            self.cambioaceite = nuevo_cambiodaceite
                        elif modificacion == "3":
                            nuevo_cambiofrenos = input("Nuevo Cambio de Frenos (S/N): ")
                            cursor.execute("UPDATE revisiones SET cambiofrenos = %s WHERE no_revision = %s", (nuevo_cambiofrenos, self.no_revision))
                            self.cambiofrenos = nuevo_cambiofrenos
                        elif modificacion == "4":
                            nuevos_otros = input("Otros cambios: ")
                            cursor.execute("UPDATE revisiones SET otros = %s WHERE no_revision = %s", (nuevos_otros, self.no_revision))
                            self.otros = nuevos_otros
                        elif modificacion == "5":
                            nueva_matricula = input("Nueva Matrícula: ")
                            cursor.execute("UPDATE revisiones SET matricula = %s WHERE no_revision = %s", (nueva_matricula, self.no_revision))
                            self.matricula = nueva_matricula
                        elif modificacion == "6":
                            nuevo_cambiodfiltro = input("Nuevo Cambio de Filtro (S/N): ")
                            nuevo_cambiodaceite = input("Nuevo Cambio de Aceite (S/N): ")
                            nuevo_cambiofrenos = input("Nuevo Cambio de Frenos (S/N): ")
                            nuevos_otros = input("Otros cambios: ")
                            nueva_matricula = input("Nueva Matrícula: ")

                            cursor.execute('''
                                UPDATE revisiones
                                SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s
                                WHERE no_revision = %s
                            ''', (nuevo_cambiodfiltro, nuevo_cambiodaceite, nuevo_cambiofrenos, nuevos_otros, nueva_matricula, self.no_revision))
                            
                            self.cambiofiltro = nuevo_cambiodfiltro
                            self.cambioaceite = nuevo_cambiodaceite
                            self.cambiofrenos = nuevo_cambiofrenos
                            self.otros = nuevos_otros
                            self.matricula = nueva_matricula
                        elif modificacion == "7":
                            print("Modificación cancelada.")
                            break
                        else:
                            print("Opción no válida.")
                            continue

                        conexion.commit()
                        print("Datos actualizados correctamente.")
                        break
                else:
                    print("Revisión no encontrada.")
            
            else:
                print("Opción no válida.")
                
    def eliminar_revision(self, cursor, conexion):
        while True:
            cursor.execute("SELECT * FROM revisiones")
            revisiones = cursor.fetchall()

            print("Listado de Revisiones:")
            for revision in revisiones:
                print(f"No. Revisión: {revision[0]}, Cambio de Filtro: {revision[1]}, Cambio de Aceite: {revision[2]}, Cambio de Frenos: {revision[3]}, Otros: {revision[4]}, Matrícula: {revision[5]}")

            no_revision = input("Ingrese el número de la revisión que desea eliminar o '0' para cancelar: ")

            if no_revision.isdigit():
                no_revision = int(no_revision)
                if no_revision == 0:
                    print("Cancelando operación de eliminación.")
                    break

                cursor.execute("SELECT * FROM revisiones WHERE no_revision = %s", (no_revision,))
                revision = cursor.fetchone()

                if revision:
                    cursor.execute("DELETE FROM revisiones WHERE no_revision = %s", (no_revision,))
                    conexion.commit()
                    print(f"Revisión con número {no_revision} eliminada correctamente.")
                    break
                else:
                    print("Revisión no encontrada.")
            else:
                print("Número no válido. Por favor, ingrese un número válido.")
                
    @staticmethod
    def listar_revisiones(cursor):
        cursor.execute("SELECT * FROM revisiones")
        revisiones = cursor.fetchall()

        print("Listado de Revisiones:")
        for revision in revisiones:
            print(f"No. Revisión: {revision[0]}, Cambio de Filtro: {revision[1]}, Cambio de Aceite: {revision[2]}, Cambio de Frenos: {revision[3]}, Otros: {revision[4]}, Matrícula: {revision[5]}")

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad, telefono):
        self._nif = nif
        self._nombre = nombre
        self._direccion = direccion
        self._ciudad = ciudad
        self._telefono = telefono

    def getNif(self):
        return self.nif
    def setNif(self, nif):
        self.nif = nif
        
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getCiudad(self):
        return self.ciudad
    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def getTel(self):
        return self.tel
    def setTel(self, tel):
        self.tel = tel

    def agregar_cliente(self, cursor, conexion):
        # Captura de datos
        self._nif = input("NIF del Cliente: ")
        self._nombre = input("Nombre del Cliente: ")
        self._direccion = input("Dirección del Cliente: ")
        self._ciudad = input("Ciudad del Cliente: ")
        self._telefono = input("Teléfono del Cliente: ")

        # Insertar los datos en la tabla clientes
        cursor.execute('''
            INSERT INTO clientes (nif, nombre, direccion, ciudad, tel)
            VALUES (%s, %s, %s, %s, %s)
        ''', (self._nif, self._nombre, self._direccion, self._ciudad, self._telefono))

        conexion.commit()

        print("Cliente agregado exitosamente con NIF:", self._nif)

    def listar_clientes(self, cursor, conexion):
        try:
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            
            print("Listado de Clientes:")
            for cliente in clientes:
                print(f"NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Teléfono: {cliente[4]}")
        except:
            print("No hay clientes disponibles")

    def modificar_cliente(self, cursor, conexion):
        while True:
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            
            print("Listado de Clientes:")
            for cliente in clientes:
                print(f"NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Teléfono: {cliente[4]}")
            
            nif = input("Ingrese el NIF del cliente que desea modificar o '0' para cancelar: ")

            if nif == '0':
                print("Cancelando operación de modificación.")
                break

            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (nif,))
            cliente = cursor.fetchone()

            if cliente:
                self.nif = cliente[0]
                self.nombre = cliente[1]
                self.direccion = cliente[2]
                self.ciudad = cliente[3]
                self.tel = cliente[4]
                
                while True:
                    print("Modificar datos del cliente:")
                    print("1. Nombre")
                    print("2. Dirección")
                    print("3. Ciudad")
                    print("4. Teléfono")
                    print("5. Todos")
                    print("6. Cancelar")

                    modificacion = input("Elija la opción a modificar: ")

                    if modificacion == "1":
                        nuevo_nombre = input("Nuevo Nombre: ")
                        cursor.execute("UPDATE clientes SET nombre = %s WHERE nif = %s", (nuevo_nombre, self.nif))
                        self.nombre = nuevo_nombre
                    elif modificacion == "2":
                        nueva_direccion = input("Nueva Dirección: ")
                        cursor.execute("UPDATE clientes SET direccion = %s WHERE nif = %s", (nueva_direccion, self.nif))
                        self.direccion = nueva_direccion
                    elif modificacion == "3":
                        nueva_ciudad = input("Nueva Ciudad: ")
                        cursor.execute("UPDATE clientes SET ciudad = %s WHERE nif = %s", (nueva_ciudad, self.nif))
                        self.ciudad = nueva_ciudad
                    elif modificacion == "4":
                        nuevo_telefono = input("Nuevo Teléfono: ")
                        cursor.execute("UPDATE clientes SET tel = %s WHERE nif = %s", (nuevo_telefono, self.nif))
                        self.tel = nuevo_telefono
                    elif modificacion == "5":
                        nuevo_nombre = input("Nuevo Nombre: ")
                        nueva_direccion = input("Nueva Dirección: ")
                        nueva_ciudad = input("Nueva Ciudad: ")
                        nuevo_telefono = input("Nuevo Teléfono: ")

                        cursor.execute('''
                            UPDATE clientes
                            SET nombre = %s, direccion = %s, ciudad = %s, tel = %s
                            WHERE nif = %s
                        ''', (nuevo_nombre, nueva_direccion, nueva_ciudad, nuevo_telefono, self.nif))
                        
                        self.nombre = nuevo_nombre
                        self.direccion = nueva_direccion
                        self.ciudad = nueva_ciudad
                        self.tel = nuevo_telefono
                    elif modificacion == "6":
                        print("Modificación cancelada.")
                        break
                    else:
                        print("Opción no válida.")
                        continue

                    conexion.commit()
                    print("Datos actualizados correctamente.")
                    break
            else:
                print("Cliente no encontrado.")

                
    def eliminar_cliente(self, cursor, conexion):
        while True:
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            
            print("Listado de Clientes:")
            for cliente in clientes:
                print(f"NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Teléfono: {cliente[4]}")

            nif = input("Ingrese el NIF del cliente que desea eliminar o '0' para cancelar: ")

            if nif == '0':
                print("Cancelando operación de eliminación.")
                break

            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (nif,))
            cliente = cursor.fetchone()

            if cliente:
                cursor.execute("DELETE FROM clientes WHERE nif = %s", (nif,))
                conexion.commit()
                print(f"Cliente con NIF {nif} eliminado correctamente.")
                break
            else:
                print("Cliente no encontrado.")
                

