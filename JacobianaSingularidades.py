import numpy as np
import matplotlib.pyplot as plt


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
    b = np.array([[3, 2, 1, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
    c = np.linalg.pinv(b)
    # print(inv(a))
    # print(b)
    # print(np.linalg.det(b))
    # print(c)
    # print(np.around(c, 4))
    d = np.linalg.multi_dot([b, c, b])
    # print(d)
    # print(np.around(d))
    # print(inv(b))
    #figure, _ = plt.subplots()
    # plt.show(figure)
    #plt.matshow(b)
    # plt.colorbar()
    # plt.matshow(np.random.random((50, 50)))
    # plt.imshow(np.random.random((50, 50)))
    plt.figure()
    plt.plot(d)
    plt.show()
