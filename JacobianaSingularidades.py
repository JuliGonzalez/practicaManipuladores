import numpy as np
import matplotlib.pyplot as plt

from Jacobiana import Jacobiana
from CinematicaDirecta import CinematicaDirecta


class JacobianaSingularidades:
    def __init__(self, a1, theta1, theta2, d3):
        self.a1 = a1
        self.theta1 = theta1
        self.theta2 = theta2
        self.d3 = d3
        self.jacobiana = Jacobiana(self.a1)
        self.cinematica = CinematicaDirecta()
        self.pos_actual = np.array([[]], dtype=np.float)
        self.pos_final = np.array([[]], dtype=np.float)
        self.pos_primer_segmento = np.array([[]], dtype=np.float)
        self.en_movimiento = True

    def get_matriz_transformacion(self):  # matriz a30
        return np.linalg.multi_dot(
            [self.cinematica.transform_matrix(self.a1, 0, self.theta1, 0), self.cinematica.transform_matrix(
                0, 0, self.theta2 + np.pi / 2, np.pi / 2),
             self.cinematica.transform_matrix(0, self.d3, 0, 0)])

    def get_pos_primer_segmento(self):  # matriz a20
        return np.linalg.multi_dot(
            [self.cinematica.transform_matrix(self.a1, 0, self.theta1, 0), self.cinematica.transform_matrix(
                0, 0, self.theta2 + np.pi / 2, np.pi / 2)
             ])

    def get_jacobiana(self):
        return self.jacobiana.matriz_jacobiana(self.theta1, self.theta2, self.d3)[[0, 1, 5], :]

    def comprobacion_singularidad(self, matriz):
        if np.linalg.det(matriz) == 0:
            return np.linalg.pinv(matriz)
        else:
            return np.linalg.inv(matriz)

    def multiplicacion_inversa(self, matriz, velocidades):
        return np.dot(matriz, np.transpose(velocidades))[:, None]

    def actualizar_thetas(self, deltatheta):
        deltatheta1 = deltatheta[0, 0]
        deltatheta2 = deltatheta[1, 0]
        self.theta1 += deltatheta1
        self.theta2 += deltatheta2
        print("theta1")
        print(self.theta1)
        print("theta2")
        print(self.theta2)

    def mover_manipulador(self):
        self.pos_actual = self.get_matriz_transformacion()[:, [-1]]
        #self.pos_actual = self.cinematica.transform_matrix(self.d3, 0, self.theta2, 0)
        self.pos_primer_segmento = self.get_pos_primer_segmento()[:, [-1]]
        self.pos_final = np.array([[4], [0.5], [0], [1]])
        longitud = self.a1 + self.d3
        distPerUpdate = 0.02 * longitud
        # vector_target = pos_final - pos_actual (brazo del robot segun la transformada)
        if np.linalg.norm(self.pos_final - self.pos_actual) > 0.02 * longitud:
            targetVector = (self.pos_final - self.pos_actual)[:3]
            targetUnitVector = targetVector / np.linalg.norm(targetVector)
            deltaR = distPerUpdate * targetUnitVector
            J = self.jacobiana.matriz_jacobiana_reducida(self.theta1, self.theta2, self.d3)
            Jinv = self.comprobacion_singularidad(J)
            deltatheta = Jinv.dot(deltaR)
            self.actualizar_thetas(deltatheta)
            print("primer segmento")
            print(self.pos_primer_segmento)
            print("end_Effector pos")
            print(self.pos_actual)
            plt.figure('figura inicial')
            plt.plot([0, self.pos_primer_segmento[0][0]], [0, self.pos_primer_segmento[1][0]], marker='o')  #primer segmento
            plt.plot([self.pos_primer_segmento[0][0], self.pos_actual[0][0]],  # segundo segmento
                     [self.pos_primer_segmento[1][0], self.pos_actual[1][0]],
                     marker='o')
            plt.plot([self.pos_final[0][0]], [self.pos_final[1][0]], marker='o')  # punto de destino
            plt.show()
            # circle = plt.Circle((self.a1, self.d3), self.a1 + self.d3, ls='dashed', fill=False)
        else:
            self.en_movimiento = False
        #  ax.add_artist(circle)
        # updatear coordenadas del brazo
        # quizas no es necesario ya que se hace la matriz

    def update_plot(self):
        # armLine.set_data(self.pos_, Arm.joints[1, :-1])
        # endEff.set_data(Arm.joints[0, -2::], Arm.joints[1, -2::])
        pass

    def plot_manipulador(self):
        while self.en_movimiento:
            self.mover_manipulador()
        # plt.show()


if __name__ == "__main__":
    js = JacobianaSingularidades(3, 0, 0, 3)
    np.set_printoptions(suppress=True)
    jacobiana = js.get_jacobiana()
    # velocidad1 = ([0, np.pi / 90, 0])
    # print(velocidad1)
    # singularidad = js.comprobacion_singularidad(jacobiana)
    # p osicionFinal = js.jacobiana.multiplicacion(jacobiana, velocidad1)
    # print(posicionFinal)
    # result = js.multiplicacion_inversa(singularidad, velocidad1)
    # print("el resultado es: ")
    # print(result)
    js.plot_manipulador()
    """cdirecta = js.cinematica
    a20 = np.dot(cdirecta.transform_matrix(4, 0, np.pi / 4, 0), cdirecta.transform_matrix(0, 0, -np.pi / 4, np.pi / 2))

    a30 = np.linalg.multi_dot([cdirecta.transform_matrix(4, 0, np.pi / 4, 0),
                               cdirecta.transform_matrix(0, 0, -np.pi / 4, np.pi / 2),
                               cdirecta.transform_matrix(0, 3, 0, 0)])
    l1 = 5
    l2 = 10
    x1 = l1 * np.cos(np.pi / 3)
    y1 = l2 * np.sin(np.pi / 4)
    plt.figure()
    plt.plot([0, a20.item(3)], [0, a20.item(7)], marker='o')
    plt.plot([a20.item(3), a30.item(3)], [a20.item(7), a30.item(7)], marker='o')"""
