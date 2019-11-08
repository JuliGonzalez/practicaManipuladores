
import numpy as np
import math


class CinematicaDirecta:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        # no se qe poner aqui

    def cinematica_directa(self, a, b, c):
        return np.array([
            # primera fila:
            [math.cos(a) * math.cos(b) - math.sin(a) * math.sin(b),
             -math.cos(a) * math.sin(b) - math.sin(a) * math.cos(b),
             0,
             c * math.cos(a) * math.cos(b) - c * math.sin(a) * math.sin(b) + self.a2 * math.cos(
                 a) * math.cos(b) - self.a2 * math.sin(a) * math.sin(b) + self.a1 * math.cos(a)],
            # segunda fila:
            [math.sin(a) * math.cos(b) + math.cos(a) * math.sin(b),
             -math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b),
             0,
             c * math.sin(a) * math.sin(b) + c * math.cos(a) * math.sin(b) + self.a2 * math.sin(
                 a) * math.cos(b) + self.a2 * math.cos(a) * math.sin(b) + self.a1 * math.sin(a)],
            # tercera fila
            [0, 0, 1, 0],
            # cuarta fila
            [0, 0, 0, 1]])


if __name__ == "__main__":
    cinematica1 = CinematicaDirecta(0.5, 0.5, 0)
    #cinematica2 = Cinematica_directa(0.7, 0.8)
    print("primera matriz")
    print(cinematica1.cinematica_directa(0, 0, 0))
    print("segunda matriz")
    print(cinematica1.cinematica_directa(0, np.pi / 2, 0))
    print("tercera matriz")
    print(cinematica1.cinematica_directa(-np.pi / 2, np.pi / 2, 0.2))
    print("cuarta matriz")
    print(cinematica1.cinematica_directa(np.pi, 0, 0.4 / 2))



