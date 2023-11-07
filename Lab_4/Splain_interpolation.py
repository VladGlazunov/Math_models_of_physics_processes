import math


def sep_P(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x ** 1 + d


def d_sep_P(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x ** 1 + c * x ** 0


def Splain_violence(lst):
    y_list = lst[1]
    x_list = lst[0]
    matrix_kf = []
    for row_1 in range(0, len(x_list) - 1):  # начальная матрица коэф.
        row = []
        for coloumn_1 in range(4):
            row.append(1)
        matrix_kf.append(row)

    matrix_working = []
    for i in range(0, 9):
        for j in range(i, i + 2):
            row = []
            for coloumn in range(0, 5):
                if coloumn != 4:
                    row.append(x_list[j] ** (3 - coloumn))
                else:
                    row.append(y_list[j])
            matrix_working.append(row)
    return matrix_working


start_list = [[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5],
              [0.84, 1.00, 0.91, 0.6, 0.14, -0.35, -0.76, -0.98, -0.96, -0.71]]
# start_list = [[1.6, 1.7, 1.8, 1.9, 2], [1.6416, 2.3961, 3.3536, 4.5441, 6]]
print(Splain_violence(start_list))
