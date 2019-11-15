import numpy as np
import matplotlib.pyplot as plt

from Jacobiana import Jacobiana


class JacobianaSingularidades:
    def __init__(self, a1):
        self.a1 = a1
        self.jacobiana = Jacobiana(self.a1)

    def get_jacobiana(self, a, b, c):
        return self.jacobiana.matriz_jacobiana(a, b, c)

    @staticmethod
    def comprobacion_singularidad(self, matriz):
        if np.linalg.det(matriz) == 0:
            print("Determinante 0 por lo que no es una singularidad?")
            print("retornando la matriz pseudoinversa")
            return np.linalg.pinv(matriz)
        else:
            return np.linalg.inv(matriz)

    @staticmethod
    def calculoVelocidades(self, matriz, velocidades):
        return np.linalg.multi_dot([matriz, velocidades])


if __name__ == "__main__":
    js = JacobianaSingularidades(1)
    # print(inv(js.pruebas()))
    b = np.array([[3, 2, 1, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
    c = np.linalg.pinv(b)
    # print(inv(a))
    # print(b)
    # print(np.linalg.det(b))
    # print(c)
    # print(np.around(c, 4))
    d = np.linalg.multi_dot([b, c, b])
    print(np.round(d))
    # print(inv(b))
    #figure, _ = plt.subplots()
    # plt.show(figure)
    #plt.matshow(b)
    # plt.colorbar()
    # plt.matshow(np.random.random((50, 50)))
    # plt.imshow(np.random.random((50, 50)))
    plt.figure()
    #plt.plot(x, d, '-b', label='Matriz')
    plt.plot(d, label='Matrix')
    # figure1.set_xlabel('distance (m)')
    # figure1.set_ylabel('Damped oscillation')
    plt.show()
