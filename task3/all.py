import matplotlib.pyplot as plt

# Метод Эйлера
def euler_method(func, y0, x0, xn, h):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < xn:
        x_n = x_values[-1]
        y_n = y_values[-1]
        y_n1 = y_n + h * func(x_n, y_n)

        x_values.append(x_n + h)
        y_values.append(y_n1)

    return x_values, y_values

# Дифференциальное уравнение
def differential_equation(x, y):
    return 5 + x - y

# Модифицированный метод Эйлера
def modified_euler_method(x0, y0, xn, h):
    values = []

    x = x0
    y = y0

    while x <= xn:
        values.append((x, y))
        y_pred = y + h * differential_equation(x, y)
        y = y + h / 2 * (differential_equation(x, y) + differential_equation(x + h, y_pred))
        x += h

    return values

# Метод Рунге-Кутта
def runge_kutta(f, x0, y0, h, x_end):
    result = []
    x = x0
    y = y0

    while x <= x_end:
        result.append((x, y))
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

    return result

# Параметры
x0 = 2
y0 = 1
xn = 4
h = 0.5

# Выполнение методов
euler_result = euler_method(differential_equation, y0, x0, xn, h)
modified_euler_result = modified_euler_method(x0, y0, xn, h)
runge_kutta_result = runge_kutta(differential_equation, x0, y0, h, xn)

# Построение графика
x_euler, y_euler = zip(*euler_result)
x_modified_euler, y_modified_euler = zip(*modified_euler_result)
x_runge_kutta, y_runge_kutta = zip(*runge_kutta_result)

plt.plot(x_euler, y_euler, label='Метод Эйлера')
plt.plot(x_modified_euler, y_modified_euler, label='Модифицированный Эйлер')
plt.plot(x_runge_kutta, y_runge_kutta, label='Метод Рунге-Кутта')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Сравнение методов решения дифференциального уравнения')
plt.legend()
plt.grid(True)
plt.show()
