import numpy as np
from numpy.linalg import inv


class JacobianaSingularidades:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def pruebas(self):
        return np.array([[3, 2, 1, 0], [1, 2, 3, 4], [5, 2, 5, 8], [9, 8, 7, 6]])


if __name__ == "__main__":
    js = JacobianaSingularidades(1, 1, 0)
    # print(inv(js.pruebas()))
    a = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
    b = np.array([[3, 2, 1, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
    print(a)
    # print(inv(a))
    print(b)
    print(np.linalg.det(b))
    # print(inv(b))
