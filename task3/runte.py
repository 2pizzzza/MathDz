import matplotlib.pyplot as plt


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


def differential_equation(x, y):
    return 5 + x - y


x0 = 2
y0 = 1
h = 0.5
x_end = 4

solution = runge_kutta(differential_equation, x0, y0, h, x_end)

print("x\t\t y")
for x, y in solution:
    print(f"{x}\t\t {y}")

x_values = [x for x, y in solution]
y_values = [y for x, y in solution]

plt.plot(x_values, y_values, label='Решение методом Рунге-Кутта')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Решение дифференциального уравнения')
plt.legend()
plt.grid(True)
plt.show()
