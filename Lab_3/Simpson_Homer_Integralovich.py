import numpy as np


def F(x):
    return 3 * x ** 2 - x ** (1 / 2)


def Homer(a, b, fault):
    answer = 0
    for i in np.arange(a, b, fault):
        answer += (F(i) + 4 * F((2 * i + fault)/2) + F(i + fault)) / 6 * fault
    return answer


# 23.535898384862245412945107316988255266114389492379238743888386041
print(Homer(0, 3, 0.001))
