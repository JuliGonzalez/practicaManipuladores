
import numpy as np
import math


class CinematicaDirecta:
    def __init__(self, a1):
        self.a1 = a1

    def cinematica_directa(self, a, b, c):
        """
        Funcion para la obtencion de la cinematica directa
        :param a: parametro theta1
        :param b: parametro theta2
        :param c: parametro a, que sera una disntancia determinada de d3
        :return:
        """
        return np.round(np.array([
            # primera fila:
            [-math.cos(a) * math.sin(b) - math.sin(a) * math.cos(b),
             0,
             math.cos(a) * math.cos(b) - math.sin(a) * math.sin(b),
             c * math.cos(a) * math.cos(b) - c * math.sin(a) * math.sin(b) + self.a1 * math.cos(a)],
            # segunda fila:
            [-math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b),
             0,
             math.sin(a) * math.cos(b) + math.cos(a) * math.sin(b),
             c * math.sin(a) * math.cos(b) + c * math.cos(a) * math.sin(b) + self.a1 * math.sin(a)],
            # tercera fila
            [0, 1, 0, 0],
            # cuarta fila
            [0, 0, 0, 1]]))


if __name__ == "__main__":
    cinematica1 = CinematicaDirecta(4)
    #cinematica2 = Cinematica_directa(0.7, 0.8)
    print("primera matriz")
    print(cinematica1.cinematica_directa(0, 0, 0))
    print("segunda matriz")
    print(cinematica1.cinematica_directa(0, np.pi / 2, 0))
    print("tercera matriz")
    print(cinematica1.cinematica_directa(-np.pi / 2, np.pi / 2, 2))
    print("cuarta matriz")
    print(cinematica1.cinematica_directa(np.pi, 0, 2))



