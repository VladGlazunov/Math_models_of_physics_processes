import math


def SINUS(x):
    return math.sin(x)


def Newton_inter(lst):
    y_list = lst[1]
    x_list = lst[0]
    high_k = [y_list[0]]
    delta_x = x_list[0] - x_list[1]
    while True:
        new_y_list = []
        for i in range(0, len(y_list) - 1):
            equel = (y_list[i] - y_list[i + 1]) / (delta_x * (len(start_list[1]) + 1 - len(y_list)))
            new_y_list.append(equel)
        high_k.append(new_y_list[0])
        if len(new_y_list) == 1:
            break
        else:
            y_list = new_y_list
    return high_k


def polinom_function(b):
    rate = Newton_inter(start_list)
    answer = rate[0]
    for i in range(0, len(rate) - 1):
        answer += Recurcia(b, i) * rate[i + 1]
    return answer


def Recurcia(b, gauss):
    if gauss == 0:
        return b - start_list[0][gauss]
    else:
        return (b - start_list[0][gauss]) * Recurcia(b, gauss - 1)


start_list = [[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5],
              [0.84, 1.00, 0.91, 0.6, 0.14, -0.35, -0.76, -0.98, -0.96, -0.71]]
# start_list = [[0, 1, 2, 3], [0, 0.5, 0.866, 1]]
x_value = float(input('Введите X, если хотите узнать Y:'))
print(polinom_function(x_value))
