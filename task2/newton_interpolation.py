import matplotlib.pyplot as plt
import numpy as np
from task2.value import x, y

def divided_differences(x_values: list[float], y_values: list[float]) -> list[float]:
    n = len(x_values)
    f = y_values.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            f[i] = (f[i] - f[i - 1]) / (x_values[i] - x_values[i - j])

    return f


def newton_interpolation(x_values: list[float], y_values: list[float], x: float) -> float:
    n = len(x_values)
    f = divided_differences(x_values, y_values)
    result = f[0]

    for i in range(1, n):
        term = f[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term

    return result


def plot_newton_interpolation(x_values: list[float], y_values: list[float], x_point: float = 3.0):
    y_interpolated = newton_interpolation(x_values, y_values, x_point)

    x_values_for_plot = np.linspace(min(x_values), max(x_values), 100)
    y_values_for_plot = [newton_interpolation(x_values, y_values, x) for x in x_values_for_plot]

    plt.scatter(x_values, y_values, label='Исходные данные')
    plt.plot(x_values_for_plot, y_values_for_plot, label=f'Интерполяция Ньютона', linestyle='dashed', color='orange')

    plt.xlabel('Объем производства')
    plt.ylabel('Затраты')
    plt.title('Интерполяция данных (Ньютон)')
    plt.legend()
    plt.show()

    print(f"Значение интерполяции полиномом Ньютона в точке {x_point}: {y_interpolated}")

plot_newton_interpolation(x, y, x_point=2.1)
