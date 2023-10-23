import math
import numpy as np


def f1(x, y):
    return x ** 2 + x - y ** 2 + 0.15


def f2(x, y):
    return x ** 2 - y + y ** 2 + 0.17


e = 0.001
x, y = 0.15, 0.17
test_1_Ya = [[2 * x + 1, -2 * y],
             [2 * x, -1 + 2 * y]]
test_2_Ya = [[-math.sin(x - 1), 1], [1, math.cos(y)]]
Yakobi = np.array(test_1_Ya)


def Newton():
    x_k, y_k = x, y
    while True:
        det_Yakobi = Yakobi[0][0] * Yakobi[1][1] - Yakobi[0][1] * Yakobi[1][0]
        matrix_F = np.array([[f1(x, y)], [f2(x, y)]], )
        if det_Yakobi == 0:
            raise Exception('Метод не работает. Определитель равен нулю')
        Yakobi[0][0], Yakobi[1][1] = Yakobi[1][1], Yakobi[0][0].copy()
        Yakobi[0][1], Yakobi[1][0] = (-1) * Yakobi[1][0], (-1) * Yakobi[0][0].copy()
        delta_values = (1 / det_Yakobi) * Yakobi.dot(matrix_F)
        x_k = x + delta_values[0][0]
        y_k = y + delta_values[1][0]
        if max(abs(delta_values[0][0]), abs(delta_values[1][0])) < e:
            break
    return [x_k, y_k]
print(Newton())
