import math
def A(k, n):
    return math.factorial(n)/math.factorial(n-k)
def C(k, n):
    return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))


print((5/12)*(7/11)+(7/12)*(5/11))