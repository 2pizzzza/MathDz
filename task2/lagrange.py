import matplotlib.pyplot as plt
import numpy as np

from task2.value import x, y
def lagrange(x: list[float], y: list[float], x0: float) -> float | None:

    if len(x) != len(y) or len(x) == 0:
        return

    n: int = len(x)

    y0: float = 0.0

    for i in range(1, n):
        l: float = y[i]
        for j in range(1, n):
            if i != j:
                l *= (x0 - x[j]) / (x[i] - x[j])

        y0 += l

    return y0

def plot_lagrange_interpolation(x_values: list[float], y_values: list[float], x_point: float = 3.0):
    y_interpolated = lagrange(x_values, y_values, x_point)

    x_values_for_plot = np.linspace(min(x_values), max(x_values), 100)
    y_values_for_plot = [lagrange(x_values, y_values, x) for x in x_values_for_plot]

    plt.scatter(x_values, y_values, label='Исходные данные')
    plt.plot(x_values_for_plot, y_values_for_plot, label=f'Интерполяция Лагранжа', linestyle='dashed', color='purple')

    plt.xlabel('Объем производства')
    plt.ylabel('Затраты')
    plt.title('Интерполяция данных (Лагранж)')
    plt.legend()
    plt.show()

    print(f"Значение интерполяции полиномом Лагранжа в точке {x_point}: {y_interpolated}")

plot_lagrange_interpolation(x, y, x_point=2.1)
