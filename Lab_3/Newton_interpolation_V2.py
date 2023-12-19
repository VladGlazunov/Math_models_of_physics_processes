import math
import numpy as np


def divided_difference(lst, k):
    x_values = lst[0]
    y_values = lst[1]
    result = 0
    for i in range(0, k + 1):
        inter_value = 1
        for j in range(0, k + 1):
            if j != i:
                inter_value *= (x_values[i] - x_values[j])
        result += y_values[i] / inter_value
    return result


def Newton_interpolation(lst, n, x):
    x_values = lst[0]
    y_values = lst[1]
    result = y_values[0]
    for i in range(1, n):
        inter_value = 1
        for j in range(0, i):
            inter_value *= (x - x_values[j])
        result += divided_difference(lst, i) * inter_value
    return result


start_list_1 = [[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5],
                [0.84, 1.00, 0.91, 0.6, 0.14, -0.35, -0.76, -0.98, -0.96, -0.71]]
new_pol = Newton_interpolation(start_list_1, len(start_list_1[0]), 4.1)
print(new_pol)