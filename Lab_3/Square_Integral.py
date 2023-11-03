import numpy as np


def F(x):
    return 3 * x ** 2 - x ** (1 / 2)


# 23.535898384862245412945107316988255266114389492379238743888386041
def Square(a, b, fault):
    answer = 0
    for i in np.arange(a, b, fault):
        answer += F((2 * i + fault) / 2) * fault
    return answer


print(Square(0, 3, 0.001))
