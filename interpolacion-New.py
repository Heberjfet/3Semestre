##heber jafet alvaro ramirez
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
def obtener_polinomio(x, y):
    local_diferencias_divididas = diferencias_divididas(x, y)
    n = len(x)
    polinomio = f"{local_diferencias_divididas[0]:.3f}"

    for i in range(1, n):
        termino = f"{local_diferencias_divididas[i]:.3f}"
        for j in range(i):
            termino += f" * (x - {x[j]:.3f})"
        polinomio += " + " + termino

        polinomio_simp = sp.sympify(polinomio)
    return sp.expand(polinomio_simp)

def diferencias_divididas(x, y):
    n = len(x)
    diferencias_divididas = [[0] * n for _ in range(n)]

    for i in range(n):
        diferencias_divididas[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            diferencias_divididas[i][j] = (diferencias_divididas[i + 1][j - 1] - diferencias_divididas[i][j - 1]) / (x[i + j] - x[i])

    return diferencias_divididas[0]

def interpolacion_newton(x, y, valor_x):
    diferencias_divididas = diferencias_divididas(x, y)
    n = len(x)
    resultado = diferencias_divididas[0]

    for i in range(1, n):
        termino = diferencias_divididas[i]
        for j in range(i):
            termino *= (valor_x - x[j])
        resultado += termino

    return resultado

n = int(input("Introduce la cantidad de coordenadas: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Introduce x[{i}]: ")))
    y.append(float(input(f"Introduce y[{i}]: ")))

valor_x = float(input("Introduce el valor inicial de x para comenzar la interpolación: "))

polinomio_interpolacion = obtener_polinomio(x, y)
print(f"El polinomio de interpolación simplificado es: P(x) = {polinomio_interpolacion}")

x_sym = sp.symbols('x')
polinomio_lambda = sp.lambdify(x_sym, polinomio_interpolacion, 'numpy')

# Aquí comienza la gráfica y la sustitición de valores
x_vals = np.linspace(min(x), max(x), 400)
y_vals = [polinomio_lambda(x_val) for x_val in x_vals]
3
plt.figure()
plt.plot(x_vals, y_vals, label=f'P(x) = {polinomio_interpolacion}')
plt.scatter(x, y, color='red', label='Datos de entrada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Polinomio de Interpolación de Newton')
plt.show()