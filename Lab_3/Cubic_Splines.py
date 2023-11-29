import math
import numpy as np


def F1(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def Th_Gauss(matrix):  # сделать так, чтобы при нуле в начале ничего не ломалось
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


def Creat_Interpolation_Matrix(lst):
    x_values = lst[0]
    y_values = lst[1]
    interval_count = len(x_values) - 1
    interpolation_matrix = [] # пустая матрица для вычисления коэффициентов
    for row_number in range(0, interval_count * 4):
        row = []
        for column_number in range(0, interval_count * 4 + 1):
            row.append(0)
        interpolation_matrix.append(row)

    # заполнение матрицы для вычисления коэффициентов
    # заполнение с учетом первого условия
    for row_number in range(0, interval_count * 2):
        for column_number in range(0, 4):
            interpolation_matrix[row_number][column_number + 4 * (math.floor(row_number / 2))] =\
                x_values[math.ceil(row_number / 2)] ** (3 - column_number)
            if column_number == 3:
                interpolation_matrix[row_number][len(interpolation_matrix[0]) - 1] = \
                    y_values[math.ceil(row_number / 2)]

    # заполнение с учетом второго условия
    for row_number in range(interval_count * 2, interval_count * 3 - 1):
        divergence_value = row_number - interval_count * 2 + 1
        for column_number in range(0, 4):
            interpolation_matrix[row_number][column_number + 4 * (divergence_value - 1)] = \
                (3 - column_number) * x_values[divergence_value] ** (2 - column_number)
        for column_number in range(4, 8):
            interpolation_matrix[row_number][column_number + 4 * (divergence_value - 1)] = \
                - (3 + (4 - column_number)) * x_values[divergence_value] ** (2 + (4 - column_number))

    # заполнение с учетом третьего условия
    for row_number in range(interval_count * 3 - 1, interval_count * 4 - 2):
        divergence_value = row_number - (interval_count * 3 - 1) + 1
        for column_number in range(0, 2):
            interpolation_matrix[row_number][column_number + 4 * (divergence_value - 1)] = \
                (6 / (3 ** column_number)) * x_values[divergence_value] ** (1 - column_number)
        for column_number in range(4, 6):
            interpolation_matrix[row_number][column_number + 4 * (divergence_value - 1)] = \
                - (6 / (3 ** (column_number - 4))) * x_values[divergence_value] ** (5 - column_number)

    point_count = interval_count - 1
    # заполнение с учетом четвертого условия
    for column_number in range(0, 2):
        interpolation_matrix[interval_count * 4 - 2][column_number] = \
            (6 / (3 ** column_number)) * x_values[0] ** (1 - column_number)
    for column_number in range(point_count * 4, point_count * 4 + 2):
        interpolation_matrix[interval_count * 4 - 1][column_number] = \
            ((6 / (3 ** (column_number - point_count * 4))) * x_values[len(x_values) - 1]
             ** (point_count * 4 + 1 - column_number))
    return interpolation_matrix


def Interpolation_Coeff(lst, x):
    Values = Th_Gauss(Creat_Interpolation_Matrix(lst))
    interval_count = len(lst[0]) - 1
    final_coeff = [] #окончательная матрица коэффициентов полиномов
    coeff_count = 0 #счетчик коэффициентов для заполнения матрицы
    for polinom_number in range(0, interval_count):
        polinom = []
        for coeff_number in range(0, 4):
            polinom.append(Values[coeff_count])
            coeff_count += 1
        final_coeff.append(polinom)

    a = lst[0][0]
    b = lst[0][interval_count]
    final_value = 0
    #подставление заданного x
    if x < a or x > b:
        raise Exception("x is out of interpolation's range")
    elif x == b:
        final_value = F1(final_coeff[interval_count - 1][0], final_coeff[interval_count - 1][1],
                         final_coeff[interval_count - 1][2], final_coeff[interval_count - 1][3], x)
    else:
        k = math.floor(x / 0.5) - 2
        final_value = F1(final_coeff[k][0], final_coeff[k][1], final_coeff[k][2], final_coeff[k][3], x)

    return final_value


start_list_1 = [[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5],
                [0.84, 1.00, 0.91, 0.6, 0.14, -0.35, -0.76, -0.98, -0.96, -0.71]]
print(Interpolation_Coeff(start_list_1, 5.1))
