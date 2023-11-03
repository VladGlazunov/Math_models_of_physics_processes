m = []


def iteration(x0, fault):
    while True:
        v0 = x0
        a_valuas = A(x0)
        x0 = (1 - a_valuas) / 3
        m.append(1)
        print("Итерация {0}. Значение промежуточных корней:".format(len(m)), x0)
        print("Итерация {0}. Значение промежуточного значения функции:".format(len(m)), f(x0), end='\n\n')
        if abs(v0 - x0) < fault:
            return x0


def f(x):
    return x ** 3 + 3 * x - 1


def A(x):
    return x ** 3


def B(x):
    return 1 - 3 * x


def cube(w0):
    if w0 < 0:
        w1 = (abs(w0)) ** (1. / 3.)
        return -w1
    else:
        return w0 ** (1. / 3.)


a = float(input('Исходное число: '))
fault = float(input('Заданная погрешность: '))

root = iteration(a, fault)
print("Корень уравнения:", root)  # x = 0.322185354626086 | Значение по вольфраму
print("Значение функции в точке:", f(root))
print("Число итераций:", len(m))
