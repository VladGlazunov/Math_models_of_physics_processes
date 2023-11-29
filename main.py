import math


def A(k, n):
    return math.factorial(n) / math.factorial(n - k)


def C(k, n):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def Puasson(n, p, k):
    answer = 0
    h = n * p
    for i in range(0, k + 1):
        answer += math.exp(-h) * (h ** i) / math.factorial(i)
    return answer


# v = 0
# for i in range(0, 9):
#     a = 1 - math.exp(-4.9 * i)
#     v += a
#     print(i, round(a, 4))
#     print(v, end='\n\n')
a = (C(1, 3)/C(1, 5) * C(1, 3)/C(1, 8) +
        C(1, 2)/C(1, 5) * C(1, 5)/C(1, 8)) * 0.5 + C(1, 3)/C(1, 5) * C(1, 5)/C(1, 8)
print(a)