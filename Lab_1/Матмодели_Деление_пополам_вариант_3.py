m = []


def find_root(function, a, b, fault):
    if function(a) * function(b) >= 0:
        raise Exception("Initial approximation error")
    while True:
        c = (a+b)/2
        a_values = function(a)
        c_values = function(c)
        m.append(1)
        if abs(c-a) < fault:
            return c
        if a_values*c_values < 0:
            b = c
        else:
            a = c
        print("Итерация {0}. Значение промежуточных корней:".format(len(m)), c)


def F(x):
    return x**3 + 3 * x - 1


print('Исследуемая область')
a = float(input())  # 1
b = float(input())  # -1

print('Заданная погрешность')
fault = float(input())  # 0.001

# j = 0.322185354626086 Значение по вольфраму

root = find_root(F, a, b, fault)
print("Корень уравнения:", root)
print("Значение функции в точке:" ,F(root))
print("Количество итераций:", len(m))