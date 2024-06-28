class Usucario:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def infoUsuario(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.tel)


class Cliente(Usucario):
    def __init__(self, nombre, direccion, tel):
        super().__init__(nombre, direccion, tel)
        self.numCliente = self._get_next_num_cliente()

    def _get_next_num_cliente(self):
        return 1

    def infoCliente(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.tel)
        print("Número de cliente: ", self.numCliente)


class Empleado(Usucario):
    def __init__(self, nombre, direccion, tel, salario, numEmpleado, tipo):
        super().__init__(nombre, direccion, tel)
        self.salario = salario
        self.numEmpleado = numEmpleado
        self.tipo = tipo

    def infoUsuario(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.tel)
        print("Salario: ", self.salario)
        print("Número de empleado: ", self.numEmpleado)
        print("Tipo de empleado: ", self.tipo)