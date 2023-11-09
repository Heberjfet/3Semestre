import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x**3 + 2

def metodo_trapecio(a, b):
    resultado = (b - a) * (funcion(a) + funcion(b)) / 2
    return resultado

# Intervalo de 0 a 1
a = 0
b = 1

# Puntos para graficar la función
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

# Calcular el área
area = metodo_trapecio(a, b)
print('Area = {:.2f}'.format(area))

# Graficar la función
plt.plot(x_vals, y_vals, label='f(x) = x^3 + 2')

# Imprimir el resultado en la gráfica
plt.text(0.1, 1.5, 'Area = {:.2f}'.format(area), verticalalignment='bottom', horizontalalignment='right', color='black', fontsize=15)

# Trapecios utilizados en la aproximación
plt.title('método del trapecio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
