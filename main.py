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
r
