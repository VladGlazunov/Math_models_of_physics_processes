def method(f, df, x0, fault):
    x1 = 0
    iter_count = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < fault:
            break
        x0 = x1
        iter_count += 1     # А почему не через множество?
        print("Итерация {0}. Значение промежуточных корней:".format(iter_count), x0)
        print("Итерация {0}. Значение промежуточного значения функции:".format(iter_count), f(x0), end='\n\n')
    return x1, iter_count + 1


def f(x):
    return x**3 + 3 * x - 1


def df(x):
    return 3 * x**2 + 3     # Ммммм... Дифференцирование вручную.


print('Исходное число')
x0 = float(input())  # 1

print('Заданная погрешность')
fault = float(input())  # 0.001

root, iterations = method(f, df, x0, fault)

print("Корень уравнения:", root)         # x = 0.322185354626086 | Значение по вольфраму
print("Значение функции в точке:",f(root))
print("Число итераций:", iterations)