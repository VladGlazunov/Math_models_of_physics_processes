import numpy as np


def F(x):
    return 3 * x ** 2 - x ** (1 / 2)


def Homer(f, a, b, fault):
    iteration = 0
    interval = (b - a) / 2
    while True:
        iteration += 1
        answer_1, answer_2 = 0, 0
        for i in np.arange(a, b, interval):
            answer_1 += (f(i) + 4 * f((2 * i + interval) / 2) + f(i + interval)) / 6 * interval
        interval /= 2
        for j in np.arange(a, b, interval):
            answer_2 += (f(j) + 4 * f((2 * j + interval) / 2) + f(j + interval)) / 6 * interval
        if abs(answer_2 - answer_1) < fault:
            return [answer_2, iteration, (b - a) / interval]


# 23.535898384862245412945107316988255266114389492379238743888386041
print(Homer(F, 0, 3, 0.001))
