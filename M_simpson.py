import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np

X = sp.Symbol("x")
while True:
    try:
        func_input = input("Ingrese la función en términos de X: ")
        function = sp.sympify(func_input)
        break
    except ValueError:
        pass

f = sp.lambdify(X, function)
lower_limit = float(input("Ingrese el límite inferior: "))
upper_limit = float(input("Ingrese el límite superior: "))
n_intervals = int(input("Ingrese el número de intervalos: "))
h = (upper_limit - lower_limit) / n_intervals
even_sum = 0
odd_sum = 0
xi = lower_limit

for i in range(1, n_intervals + 1):
    print(f"x{i} = {xi}")
    print(f"f(x{i}) = {f(xi)}" + "\n")
    if i % 2 == 0:
        even_sum += f(xi)
    elif i != 1:
        odd_sum += f(xi)
    xi += h

area = (h / 3) * (f(lower_limit) + 4 * even_sum + 2 * odd_sum + f(xi))
print(f"Área encontrada: {area}")

x_values = np.linspace(lower_limit, upper_limit, 400)
y_values = f(x_values)
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f"Función = {function}")
plt.scatter([lower_limit, upper_limit], [f(lower_limit), f(upper_limit)], color='red')
plt.fill_between(x_values, y_values, color='lightblue', alpha=0.5, label=f"Área encontrada = {area}")
plt.title('Gráfica')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
