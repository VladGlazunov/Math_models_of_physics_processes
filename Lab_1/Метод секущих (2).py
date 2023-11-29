m = []


def find_root(function, a, b, fault):
    if function(a) * function(b) >= 0:
        raise Exception("Initial approximation error")
    c1 = a
    while True:
        a_values = function(a)
        b_values = function(b)
        c2 = a - (a_values*(a-b))/(a_values-b_values)
        c_values = function(c2)
        m.append(1)
        if abs(c1 - c2) < fault:
            return c2
        elif a_values * c_values < 0:
            b = c2
        elif c_values * b_values < 0:
            a = c2
        print("Итерация {0}. Значение промежуточных корней:".format(len(m)), c2)
        print("Итерация {0}. Значение промежуточного значения функции:".format(len(m)), F(c2), end='\n\n')
        c1 = c2


def F(x):
    return x**3 + 3 * x - 1


print('Исследуемая область')
a = float(input())  # 1
b = float(input())  # -1

print('Заданная погрешность')
fault = float(input())  # 0.001

root = find_root(F, a, b, fault)
print("Корень уравнение:", root)    # x = 0.322185354626086 | Значение по вольфраму
print("Значение функции в точке:", F(root))
print("Количество итераций:", len(m))