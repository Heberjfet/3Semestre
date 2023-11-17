import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 0.1 * np.sqrt(y) + 0.4 * x**2

def euler_method(x0, y0, h, num_iterations):
    x_values = [x0]
    y_values = [y0]

    for _ in range(num_iterations):
        x = x_values[-1]
        y = y_values[-1]
        y_new = y + h * f(x, y)
        x_values.append(x + h)
        y_values.append(y_new)

    return x_values, y_values

x0 = 2
y0 = 4
h = float(input('ingrese el valor de h: '))

num_iterations = int(input('ingrese el numero de iteraciones: '))

x_values, y_values = euler_method(x0, y0, h, num_iterations)

for i in range(num_iterations + 1):
    print(f"Iteración {i}: x = {x_values[i]:.2f}, y = {y_values[i]:.4f}")

plt.plot(x_values, y_values, marker='o')
plt.title('Solución mediante el Método de Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.show()