import sympy
from sympy import simplify, cos, sin
import math
import numpy as np


class CinematicaInversa:
    def __init__(self, xe, ye, a1, phi, d3):
        self.xe = xe
        self.ye = ye
        self.a1 = a1
        self.phi = phi
        self.d3 = d3

    def get_coseno_theta2(self):
        return (self.xe **2 + self.ye**2 - (self.a1 ** 2) - (self.d3 + 1) ** 2) / (2 * self.a1 * (self.d3 + 1))

    def get_seno_theta2(self):
        return math.sqrt(1 - self.get_coseno_theta2()**2)

    def obtener_valores_inversa(self):
        print("valor de coseno")
        print(self.get_coseno_theta2())
        theta2 = np.arccos(self.get_coseno_theta2())
        print(self.get_seno_theta2())
        # theta1 = np.arcsin(self.get_seno_theta2())
        theta1 = self.phi - theta2
        return "el valor de theta1 es: %f y el valor de theta2 es: %f" % (theta1, theta2)


if __name__ == "__main__":
    # xe^2 + ye^2 de forma simbólica
    a = sympy.symbols('a_1')
    d = sympy.symbols('d_3')
    xe = sympy.symbols('x_e')
    ye = sympy.symbols('y_e')
    t1 = sympy.symbols('theta_1')
    t2 = sympy.symbols('theta_2')
    xe = d * cos(t1) * cos(t2) - d * sin(t1) * sin(t2) + a * cos(t1)
    ye = d * cos(t2) * sin(t1) + d * cos(t1) * sin(t2) + a * sin(t1)
    xe2 = xe ** 2
    ye2 = ye ** 2
    suma = xe2 + ye2
    print(simplify(suma))

    # primer caso
    inversa_caso_1 = CinematicaInversa(2, 0, 1, 0, 0)  # xe, ye, a1, phi, d3
    print(inversa_caso_1.obtener_valores_inversa())
    # segundo caso
    inversa_caso_1 = CinematicaInversa(1, 1, 1, np.pi / 2, 0)  # xe, ye, a1, phi, d3
    print(inversa_caso_1.obtener_valores_inversa())
    # tercer caso
    inversa_caso_1 = CinematicaInversa(2, -1, 1, 0, 1)  # xe, ye, a1, phi, d3
    print(inversa_caso_1.obtener_valores_inversa())
    # cuarto caso
    inversa_caso_1 = CinematicaInversa(2.5, 0, 1, np.pi, 0.5)  # xe, ye, a1, phi, d3
    print(inversa_caso_1.obtener_valores_inversa())

