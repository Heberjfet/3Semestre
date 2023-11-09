import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return x**3 + 2

def metodo_trapecio_compuesto(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = funcion(x)
    resultado = h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
    return resultado

a = float(input('Ingrese el intervalo a: '))
b = float(input('Ingrese el intervalo b: '))
n = 1

area = metodo_trapecio_compuesto(a, b, n)
print('Area = {:.2f}'.format(area))

x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x^3 + 2')
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4)
plt.fill_between([a, b], [funcion(a), funcion(b)], color='orange', alpha=0.5, label='Trapecio')
plt.text(0.1, 1.5, 'Area = {:.2f}'.format(area), verticalalignment='center', horizontalalignment='center', color='black', fontsize=15)

plt.title('Método del trapecio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
