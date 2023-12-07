import matplotlib.pyplot as plt
import numpy as np


def quadratic_approximation(x_values: list[float], y_values: list[float], x: float):
    n = len(x_values)

    sum_x = sum(x_values)
    sum_x_squared = sum(x_i ** 2 for x_i in x_values)
    sum_y = sum(y_values)
    sum_x_y = sum(x_i * y_i for x_i, y_i in zip(x_values, y_values))

    a_denominator = n * sum_x_squared - sum_x ** 2
    b_numerator = n * sum_x_y - sum_x * sum_y
    b_denominator = n * sum_x_squared - sum_x ** 2
    c_numerator = sum_y * sum_x_squared - sum_x * sum_x_y
    c_denominator = n * sum_x_squared - sum_x ** 2

    a = a_denominator / b_denominator
    b = b_numerator / b_denominator
    c = c_numerator / c_denominator

    y_approximated = a * x**2 + b * x + c

    return a, b, c, y_approximated

def plot_quadratic_approximation(x_values: list[float], y_values: list[float], volume: float = 3.0):
    a, b, c, y_approximated = quadratic_approximation(x_values, y_values, volume)


    x_values_for_plot = np.linspace(min(x_values), max(x_values), 100)
    y_values_for_plot = a * x_values_for_plot**2 + b * x_values_for_plot + c

    plt.scatter(x_values, y_values, label='Исходные данные')
    plt.plot(x_values_for_plot, y_values_for_plot, label=f'Квадратичная аппроксимация\n(a={a:.2f}, b={b:.2f}, c={c:.2f})', color='green')

    quadratic_x_values_for_plot = np.linspace(min(x_values), max(x_values), 100)
    quadratic_y_values_for_plot = a * quadratic_x_values_for_plot**2 + b * quadratic_x_values_for_plot + c
    plt.plot(quadratic_x_values_for_plot, quadratic_y_values_for_plot, linestyle='dashed', color='green')

    plt.xlabel('Объем производства')
    plt.ylabel('Затраты')
    plt.title('Зависимость затрат от объема производства (Квадратичная аппроксимация)')
    plt.legend()
    plt.show()

    print(f"{a = }, {b = }, {c = }\n")
    print(f"(Квадратичная аппроксимация) {volume} у.е равняются {y_approximated:.2f} ")

x: list[float] = [1.2, 2, 2.6, 3.2, 3.6, 4.1, 5.0, 5.9, 7.2, 7.3]
y: list[float] = [120, 250, 322, 365, 430, 480, 555, 605, 643, 675]
plot_quadratic_approximation(x, y, volume=8.0)

