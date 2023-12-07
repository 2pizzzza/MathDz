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

def differential_equation(x, y):
    return 5 + x - y


if __name__ == "__main__":
    x0 = 2
    y0 = 1
    xn = 4
    h = 0.5

    x_values, y_values = euler_method(differential_equation, y0, x0, xn, h)

    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, y = {y:.6f}")
