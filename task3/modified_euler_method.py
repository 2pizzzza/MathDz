def f(x, y):
    return 5 + x - y


def modified_euler_method(x0, y0, xn, h):
    values = []

    x = x0
    y = y0

    while x <= xn:
        values.append((x, y))
        y_pred = y + h * f(x, y)
        y = y + h / 2 * (f(x, y) + f(x + h, y_pred))
        x += h

    return values


x0 = 2
y0 = 1
xn = 4
h = 0.5

result = modified_euler_method(x0, y0, xn, h)

for x, y in result:
    print(f"x = {x:.2f}, y = {y:.6f}")
