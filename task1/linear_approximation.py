import matplotlib.pyplot as plt
import numpy as np



def linear_approximation(x_values: list[float], y_values: list[float], x: float):
    n = len(x_values)

    mean_x = sum(x_values) / n
    mean_y = sum(y_values) / n

    a = sum((x_values[i] - mean_x) * (y_values[i] - mean_y) for i in range(n)) / sum(
        (x_values[i] - mean_x) ** 2 for i in range(n))
    b = mean_y - a * mean_x

    y_approximated = a * x + b

    return a, b, y_approximated


#task_5



def plot_linear_approximation(x_values: list[float], y_values: list[float], volume: float = 3.0):
    a, b, y_approximated = linear_approximation(x_values, y_values, volume)



    x_values_for_plot = np.linspace(min(x_values), max(x_values), 100)
    y_values_for_plot = a * x_values_for_plot + b

    plt.scatter(x_values, y_values, label='Исходные данные')
    plt.plot(x_values_for_plot, y_values_for_plot, label=f'Линейная аппроксимация\n(a={a:.2f}, b={b:.2f})', color='red')

    plt.xlabel('Объем производства')
    plt.ylabel('Затраты')
    plt.title('Зависимость затрат от объема производства (Линейная аппроксимация)')
    plt.legend()
    plt.show()

    print(f"{a = }, {b = }\n")
    print(f"(Линейная аппроксимация) {volume} у.е равняются {y_approximated:.2f} ")


x: list[float] = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y: list[float] = [11, 22.1, 33.2, 44, 55.2, 66.3, 77.5, 60.3, 87.9, 110]

plot_linear_approximation(x, y, volume=900.0)
