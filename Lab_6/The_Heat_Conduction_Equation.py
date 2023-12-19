import math
import numpy as np

# Начальные условия:
# T(0, x) = T_комн
# T(0, 0) = T_плав / 2
# Граничные условия:
# T(t, L) = T_комн
# T(t, 0) = T_плав / 2

# Cu
# T_плав = 1356
# k = 373
# c = 386

def Heat_Cond_Equation(del_x, del_t, t, l):
    # Значение всех данных
    T_room = 15
    T_melt = 1083 / 2
    k = 3.73

    # Grid
    h = k * del_t / (del_x ** 2)
    grid = []
    for i in np.arange(0, t / del_t + 1):
        row = []
        for j in np.arange(0, l / del_x + 1):
            row.append(0)
        grid.append(row)
    for row_number in range(-1, len(grid) - 1):
        for column_number in range(0, len(grid[row_number])):
            if column_number == 0:
                grid[row_number + 1][column_number] = T_melt
            elif (column_number == len(grid[row_number]) - 1) or (row_number == -1):
                grid[row_number + 1][column_number] = T_room
            else:
                T_1 = grid[row_number][column_number]
                T_2 = grid[row_number][column_number + 1]
                T_3 = grid[row_number][column_number - 1]
                grid[row_number + 1][column_number] = T_1 + h * (T_2 - 2 * T_1 + T_3)

    return grid

del_x = 2
del_t = 0.2
t, l = 10, 10


final_list = Heat_Cond_Equation(del_x, del_t, t, l)
for item in final_list:
    print(f'{item}')