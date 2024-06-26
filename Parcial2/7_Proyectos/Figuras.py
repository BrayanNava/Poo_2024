import math

class Figuras:
    def calcular_Area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Rectangulo(Figuras):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def get_largo(self):
        return self.largo

    def set_largo(self, largo):
        self.largo = largo

    def get_ancho(self):
        return self.ancho

    def set_ancho(self, ancho):
        self.ancho = ancho

    def calcular_Area(self):
        return self.largo * self.ancho

class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio

    def calcular_Area(self):
        import math
        return math.pi * (self.radio ** 2)

class Triangulo(Figuras):
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_ancho(self):
        return self.ancho

    def set_ancho(self, ancho):
        self.ancho = ancho

    def calcular_Area(self):
        return (self.ancho * self.altura) / 2