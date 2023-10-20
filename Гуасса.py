import numpy as np

test1 = [[1, 2, -1, -1, 0],
         [2, 3, -1, 1, 3],
         [2, 5, 2, 1, 3],
         [3, 5, 1, 2, 5]]

test2 = [[0, 1, 1, 2, 2],
         [1, 3, 2, -1, 2],
         [2, -1, 5, 3, -1],
         [4, 5, 4, -4, 8]]

hod = np.array(test2)
print(hod, end='\n\n')


def Th_Gauss():  # сделать так, чтобы при нуле в начале ничего не ломалось
    for row_number in range(0, len(hod)):
        if hod[row_number][row_number] == 0:
            hod[row_number], hod[len(hod)] = hod[len(hod)], hod[row_number]
        for next_row_number in range(row_number + 1, len(hod)):
            k = hod[next_row_number][row_number] / hod[row_number][row_number]
            for column_number in range(row_number, len(hod) + 1):
                hod[next_row_number][column_number] = hod[next_row_number][column_number] - k * hod[row_number][column_number]
    print(hod)

    xs = [0] * len(hod)
    for x_number in range(len(hod) - 1, -1, -1):
        summa = 0
        for previous_x_number in range(len(hod) - 1, x_number, -1):
            summa += xs[previous_x_number] * hod[x_number][previous_x_number]
        xs[x_number] = (hod[x_number][len(hod)] - summa) / hod[x_number][x_number]
        print(x_number, xs[x_number])
    return xs
    #
    # x3 = hod[3][4] / hod[3][3]
    # x2 = (hod[2][4] - hod[2][3] * x3) / hod[2][2]
    # x1 = (hod[1][4] - hod[1][2] * x2 - hod[1][3] * x3) / hod[1][1]
    # x0 = (hod[0][4] - hod[0][1] * x1 - hod[0][2] * x2 - hod[0][3] * x3) / hod[0][0]
    # return [x1, x2, x3, x4]


print(Th_Gauss())
