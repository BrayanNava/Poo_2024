from Figuras import *

rectangulo = Rectangulo(largo=5, ancho=3)
print(f"Rectángulo: largo={rectangulo.get_largo()}, ancho={rectangulo.get_ancho()}, área={rectangulo.calcular_Area()}")

circulo = Circulo(radio=4)
print(f"Círculo: radio={circulo.get_radio()}, área={circulo.calcular_Area()}")

triangulo = Triangulo(altura=6, ancho=4)
print(f"Triángulo: altura={triangulo.get_altura()}, ancho={triangulo.get_ancho()}, área={triangulo.calcular_Area()}")