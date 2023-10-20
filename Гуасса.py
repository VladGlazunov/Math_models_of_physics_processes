import numpy as np

hod = np.array([[1, 2, -1, -1, 0],
                [2, 3, -1, 1, 3],
                [2, 5, 2, 1, 3],
                [3, 5, 1, 2, 5]])
print(hod, end='\n\n')


def Th_Gauss():  # сделать так, чтобы при нуле в начале ничего не ломалось
    for i in range(0, 4):
        for n in range(i + 1, 4):
            y = hod[n][i].copy()
            for m in range(i, 5):
                hod[n][m] = hod[n][m] - (y / hod[i][i]) * hod[i][m]
    print(hod)

    xs = [-10000] * len(hod)
    for x_number in range(len(hod) - 1, 0, -1):
        summa = 0
        for j in range(len(hod) - 1, i, -1):
            summa += xs[j] * hod[x_number][j]
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
