import numpy as np
import math


class CinematicaDirecta:
    def __init__(self):
        pass

    def transform_matrix(self, a, d, theta, alfa):
        return np.array([
            [np.cos(theta), -np.cos(alfa) * np.sin(theta), np.sin(alfa) * np.sin(theta), a * np.cos(theta)],
            [np.sin(theta), np.cos(alfa) * np.cos(theta), -np.sin(alfa) * np.cos(theta), a * np.sin(theta)],
            [0, np.sin(alfa), np.cos(alfa), d],
            [0, 0, 0, 1]]
        )


if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    cinematica1 = CinematicaDirecta()
    # primer caso q(0,0,0)
    print(np.linalg.multi_dot(
        [cinematica1.transform_matrix(4, 0, 0, 0), cinematica1.transform_matrix(0, 0, np.pi / 2, np.pi / 2),
         cinematica1.transform_matrix(0, 0, 0, 0)]))
    # segundo caso q(0, pi/2, 0)
    print(np.linalg.multi_dot(
        [cinematica1.transform_matrix(4, 0, 0, 0), cinematica1.transform_matrix(0, 0, np.pi, np.pi / 2),
         cinematica1.transform_matrix(0, 0, 0, 0)]))
    # tercer caso q(-pi/2, pi/2, a)
    print(np.linalg.multi_dot(
        [cinematica1.transform_matrix(4, 0, -np.pi / 2, 0), cinematica1.transform_matrix(0, 0, np.pi, np.pi / 2),
         cinematica1.transform_matrix(0, 6, 0, 0)]))
    # cuarto caso q(pi, 0, a/2)
    print(np.linalg.multi_dot(
        [cinematica1.transform_matrix(4, 0, np.pi, 0), cinematica1.transform_matrix(0, 0, np.pi / 2, np.pi / 2),
         cinematica1.transform_matrix(0, 3, 0, 0)]))


