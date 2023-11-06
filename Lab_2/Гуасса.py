import numpy as np

test1 = [[1, 2, -1, -1, 0],
         [2, 3, -1, 1, 3],
         [2, 5, 2, 1, 3],
         [3, 5, 1, 2, 5]]

test2 = [[4, 1, 1, 2, 2],
         [1, 3, 2, -1, 2],
         [2, -1, 5, 3, -1],
         [4, 5, 4, -4, 8]]


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


print(Th_Gauss(test1))
