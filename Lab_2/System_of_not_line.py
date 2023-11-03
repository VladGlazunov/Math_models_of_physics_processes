import math
import numpy as np


def f1(x, y):
    return math.cos(x - 1) + y - 0.5


def f2(x, y):
    return x - math.cos(y) - 3


def Th_Gauss(matrix):
    hod = np.array(matrix)
    n = len(hod)
    for row_number in range(0, n):
        if hod[row_number][row_number] == 0:
            row_to_exchange = -10
            for a_a in range(row_number + 1, n):
                if hod[a_a, row_number] != 0:
                    row_to_exchange = a_a
                    break
            if row_to_exchange == -10:
                raise Exception("слишком много решений")
            hod[row_number], hod[row_to_exchange] = hod[row_to_exchange], hod[row_number].copy()
        for next_row_number in range(row_number + 1, n):
            k = hod[next_row_number][row_number] / hod[row_number][row_number]
            for column_number in range(row_number, n + 1):
                hod[next_row_number][column_number] = hod[next_row_number][column_number] - k * hod[row_number][
                    column_number]
    xs = [0] * n
    for x_number in range(n - 1, -1, -1):
        summa = 0
        for previous_x_number in range(n - 1, x_number, -1):
            summa += xs[previous_x_number] * hod[x_number][previous_x_number]
        xs[x_number] = (hod[x_number][n] - summa) / hod[x_number][x_number]
    return xs


def Newton():
    iteracia = []
    x_k, y_k = x, y
    while True:
        iteracia.append(1)
        matrix = []
        for row_number in range(0, len(Yakobi)):
            row = []
            matrix.append(row)
            for column_number in range(0, len(Yakobi[0])):
                matrix[row_number].append(Yakobi[row_number][column_number])
            matrix[row_number].append(-fun_mat[row_number](x_k, y_k))
        delta_answers = Th_Gauss(matrix)
        x_k, y_k = x_k + delta_answers[0], y_k + delta_answers[1]
        if max(abs(delta_answers[0]), abs(delta_answers[1])) < fault:
            break
    return [x_k, y_k, len(iteracia)]


fault = 0.001
x, y = 1, 1
test_1_Ya = [[2 * x + 1, -2 * y],
             [2 * x, -1 + 2 * y]]
test_2_Ya = [[-math.sin(x - 1), 1],
             [1, math.cos(y)]]
Yakobi = np.array(test_2_Ya)

fun_mat = [f1, f2]

for number_value in range(0, len(Newton())):
    if number_value == len(Newton()) - 1:
        print("Число итераций:", Newton()[number_value])
    else:
        print("{0} Корень системы уравнений:".format(number_value + 1), Newton()[number_value])