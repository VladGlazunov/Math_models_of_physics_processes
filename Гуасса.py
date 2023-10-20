import numpy as np
hod = np.array([[1, 2, -1, -1, 0], [2, 3, -1, 1, 3],
                  [2, 5, 2, 1, 3], [3, 5, 1, 2, 5]])
print(hod, end='\n\n')
def Th_Gauss(): #сделать так, чтобы при нуле в начале ничего не ломалось
    for i in range(0, 4):
        if i == 0:
            x = min(abs(hod[0][i]),abs(hod[1][i]), abs(hod[2][i]), abs(hod[3][i]))
        elif i == 1:
            x = min(abs(hod[1][i]), abs(hod[2][i]), abs(hod[3][i]))
        elif i == 2:
            x = min(abs(hod[2][i]), abs(hod[3][i]))
        for j in range(0, 4):
            if hod[j][i] == x:
                hod[i], hod[j] = hod[j], hod[i].copy()
                break

        for n in range(i + 1, 4):
            y = hod[n][i].copy()
            for m in range(i, 5):
                hod[n][m] = hod[n][m] - (y / hod[i][i]) * hod[i][m]
    print(hod)
    x4 = hod[3][4] / hod[3][3]
    x3 = (hod[2][4] - hod[2][3] * x4) / hod[2][2]
    x2 = (hod[1][4] - hod[1][2] * x3 - hod[1][3] * x4) / hod[1][1]
    x1 = (hod[0][4] - hod[0][1] * x2 - hod[0][2] * x3 - hod[0][3] * x4) / hod[0][0]
    return [x1, x2, x3, x4]

# print('Введите количество аргументов')
# argument = int(input())
#
# print('Введите количество строк')
# line = int(input())
# if argument < line:



print(Th_Gauss())
