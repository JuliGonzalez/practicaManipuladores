import numpy as np


class Jacobiana:
    def __init__(self, a1):
        self.a1 = a1

    def matriz_jacobiana(self, a, b, c):
        return np.array([
            [-c * np.sin(a) * np.cos(b) - c * np.cos(a) * np.sin(b) - self.a1 * np.sin(a),
             -c * np.cos(a) * np.sin(b) - c * np.sin(a) * np.cos(b),
             np.cos(a) * np.cos(b) - np.sin(a) * np.sin(b)],
            [-c * np.cos(a) * np.cos(b) - c * np.sin(a) * np.sin(b) + self.a1 * np.cos(a),
             -c * np.sin(a) * np.sin(b) + c * np.cos(a) * np.cos(b),
             np.sin(a) * np.cos(b) + np.cos(a) * np.sin(b)],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 0]
        ])

    def matriz_jacobiana_reducida(self, a, b, c): #theta1, theta2 y d3
        return np.array([
            [-c * np.sin(a) * np.cos(b) - c * np.cos(a) * np.sin(b) - self.a1 * np.sin(a),
             -c * np.cos(a) * np.sin(b) - c * np.sin(a) * np.cos(b),
             np.cos(a) * np.cos(b) - np.sin(a) * np.sin(b)],
            [-c * np.cos(a) * np.cos(b) - c * np.sin(a) * np.sin(b) + self.a1 * np.cos(a),
             -c * np.sin(a) * np.sin(b) + c * np.cos(a) * np.cos(b),
             np.sin(a) * np.cos(b) + np.cos(a) * np.sin(b)],
            [1, 1, 0]
        ])

    def multiplicacion(self, m1, m2):
        r = np.dot(m1, m2)
        return r[:, None]


if __name__ == "__main__":
    jacobiana = Jacobiana(4)
    # casos de estudio de velocidades
    # consideramos a1=4 y a=6 para los ejemplos
    caso1 = np.array([0, np.pi/90, 0])
    caso2 = np.array([-np.pi / 90, np.pi / 90, 0])
    caso3 = np.array([np.pi / 90, -np.pi / 90, 6/100])
    caso4 = np.array([np.pi / 90, 0, -6/100])

    print(jacobiana.multiplicacion(jacobiana.matriz_jacobiana(0, 0, 3), caso1))
    print(jacobiana.multiplicacion(jacobiana.matriz_jacobiana(np.pi / 4, -np.pi / 4, 0), caso2))
    print(jacobiana.multiplicacion(jacobiana.matriz_jacobiana(-np.pi / 4, np.pi / 4, 0), caso3))
    print(jacobiana.multiplicacion(jacobiana.matriz_jacobiana(0, np.pi/2, 3), caso4))

