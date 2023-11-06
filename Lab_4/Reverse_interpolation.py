import math


def SINUS(x):
    return math.sin(x)


def Lagrange(lst, x):
    y_list = lst[1]
    x_list = lst[0]
    answer = 0
    for i in range(0, len(y_list)):
        changing_x = 1
        for j in range(0, len(x_list)):
            if i != j:
                delta_fun = (x - x_list[j]) / (x_list[i] - x_list[j])
                changing_x *= delta_fun
        answer += y_list[i] * changing_x
    return answer


start_list = [[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5],
             [0.84, 1.00, 0.91, 0.6, 0.14, -0.35, -0.76, -0.98, -0.96, -0.71]]
# start_list = [[1.6, 1.7, 1.8, 1.9, 2], [1.6416, 2.3961, 3.3536, 4.5441, 6]]
print(Lagrange(start_list, 5.499999))
