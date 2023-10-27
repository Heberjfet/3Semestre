import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return x**2

# Definimos los límites de integración
a = 0
b = 1

# Definimos el número de subintervalos
n = 10

# Creamos una lista con los puntos x
x = np.linspace(a, b, n+1)

# Evaluamos la función en los puntos x
y = f(x)

# Graficamos la función y los trapecios
plt.plot(x, y, 'b')
plt.fill_between(x, y, 0, alpha=0.2)

# Calculamos el área bajo la curva utilizando el método del trapecio
area = np.trapz(y, x)

# Mostramos el resultado
print("El área bajo la curva es:", area)
