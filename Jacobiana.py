""" Funcion que implementa la cinematica inversa del manipulador que recibe tres argumentos (posicion de la
mano en el plano y su orientacipn) y devuelve una lista con todos los posibles valores de parametros de cada
articulacion que llevan al manipulador a esas posiciones. Deberia probarse al menos con los casos de estudio del
apartado anterior. """

import numpy as np
import math


class Jacobiana:
    def __init__(self, a1):
        self.a1 = a1

    def matriz_jacobiana(self, a, b, c):
        return np.array([
            # primera fila
            [-c * math.sin(a) * math.cos(b) - c * math.cos(a) * math.sin(b) - self.a1 * math.sin(a),
             -c * math.cos(a) * math.sin(b) - c * math.sin(a) * math.cos(b),
             math.cos(a) * math.cos(b) - math.sin(a) * math.sin(b)],
            # segunda fila
            [-c * math.cos(a) * math.cos(b) - c * math.sin(a) * math.sin(b) + self.a1 * math.cos(a),
             -c * math.sin(a) * math.sin(b) + c * math.cos(a) * math.cos(b),
             math.sin(a) * math.cos(b) + math.cos(a) * math.sin(b)],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ])

    def velocidades(self, a, b, c):
        return np.array([a, b, c])

    def multiplicacion(self, m1, m2):
        r = np.dot(m1, m2)
        return r[:, None]

    def velocidad_cinematica_directa(self, jacobiana_matriz, velocidades):
        return np.dot(jacobiana_matriz, np.transpose(velocidades))


if __name__ == "__main__":
    jacobiana1 = Jacobiana(0.5)
    jacobiana2 = Jacobiana(4)
    caso1 = np.array([0, np.pi/90, 0])
    caso2 = np.array([-np.pi / 90, np.pi / 90, 0])
    caso3 = np.array([np.pi / 90, -np.pi / 90, -200/100])  # introducimos un valor determinado para a
    caso4 = np.array([np.pi / 90, 0, -200/100])  # introducimos un valor determinado para a
    # m1 = jacobiana2.matriz_jacobiana(np.pi/4, -np.pi/4,  0)
    m1 = jacobiana2.matriz_jacobiana(0, 0, 2)
    # print(m1)
    # m2 = jacobiana2.velocidades(-np.pi/90, np.pi/90, 0)
    m2 = jacobiana2.velocidades(0, np.pi / 90, 0)
    # print(m2)
    print(jacobiana2.multiplicacion(m1, m2))
