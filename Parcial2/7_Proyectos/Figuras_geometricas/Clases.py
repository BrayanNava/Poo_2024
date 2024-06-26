import math

class Figuras:
    def estaVisible(self):
        return self._visible

    def mostrar(self):
        self._visible = True

    def ocultar(self):
        self._visible = False

    def mover(self, x, y):
        self._x = x
        self._y = y

    def calcular_Area(self):
        raise NotImplementedError("")

class Rectangulo(Figuras):
    def __init__(self, largo, ancho, x=0, y=0, visible=True):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self._x = x
        self._y = y
        self._visible = visible

    def getLargo(self):
        return self.largo

    def setLargo(self, largo):
        self.largo = largo

    def getAncho(self):
        return self.ancho

    def setAncho(self, ancho):
        self.ancho = ancho

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y

    def getVisible(self):
        return self._visible

    def setVisible(self, visible):
        self._visible = visible

    def calcular_Area(self):
        return self.largo * self.ancho

    def getInfo(self):
        print(f"El rectángulo tiene {self.getLargo()} cm de largo y {self.getAncho()} cm de ancho , X vale {self.getX()} y Y vale {self.getY()} y es {self.getVisible()}\n Su area es de {self.largo * self.ancho}") 



class Circulo(Figuras):
    def __init__(self, radio, x=0, y=0, visible=True):
        super().__init__()
        self.radio = radio
        self._x = x
        self._y = y
        self._visible = visible

    def getRadio(self):
        return self.radio

    def setRadio(self, radio):
        self.radio = radio

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y

    def getVisible(self):
        return self._visible

    def setVisible(self, visible):
        self._visible = visible

    def getArea(self):
        return self.calcularArea()

    def setArea(self, area):
        self.calcularArea=area

    def calcular_Area(self):
        return math.pi * self.radio ** 2

    def getInfo(self):
        print(f"El círculo tiene {self.getRadio()} de radio\n X vale {self.getX()} y Y vale {self.getY()} y es {self.getVisible()}\n Su area es de {math.pi * self.radio ** 2}")

