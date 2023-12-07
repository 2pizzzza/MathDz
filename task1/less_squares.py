import matplotlib.pyplot as plt
import numpy as np
from task1.value import x, y


def less_squares(x_values: list[float], y_values: list[float], x: float) -> tuple[float] or None:
    if len(y_values) != len(x_values) or len(x_values) == 0:
        return

    n: int = len(x_values)
    a: float
    b: float

    xy_sum: float = 0

    x_sum: float = 0
    y_sum: float = 0
    x_sq_sum: float = 0

    for i in range(n):
        xy_sum += x_values[i] * y_values[i]
        x_sum += x_values[i]
        y_sum += y_values[i]
        x_sq_sum += x_values[i] ** 2

    sq_sum_x: float = x_sum ** 2

    a_numerator: float = n * xy_sum - x_sum * y_sum
    b_numerator: float = x_sq_sum * y_sum - x_sum * xy_sum
    denominator: float = n * x_sq_sum - sq_sum_x

    a = a_numerator / denominator
    b = b_numerator / denominator

    y_approximate = a * x + b

    return a, b, y_approximate

def plot_less_squares_approximation(x_values: list[float], y_values: list[float], volume: float = 3.0):
    a, b, costs = less_squares(x_values, y_values, volume)

    # print(f"{k = }, {b = }")
    # print(f"Затраты на производстве при {3.0} у.е равняются {costs} рублям")

    x_values_for_plot = np.linspace(min(x), max(x), 100)
    y_values_for_plot = a * x_values_for_plot + b

    plt.scatter(x, y, label='Исходные данные')
    plt.plot(x_values_for_plot, y_values_for_plot, label=f'Линия наилучшего соответствия\n(k={a:.2f}, b={b:.2f})', color='red')

    plt.xlabel('Объем производства')
    plt.ylabel('Затраты')
    plt.title('Зависимость затрат от объема производства')
    plt.legend()
    plt.show()

    print(f"{a = }, {b = }\n")
    print(f"(Аппроксимация методом наименьших квадратов) Затраты на производство при {volume} у.е равняются {costs:.2f} рублям")


plot_less_squares_approximation(x, y, volume=14.0)
