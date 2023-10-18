import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def interpolacion_lagrange(x, y):
    n = len(x)
    x_sym = sp.symbols('x')
    polinomio = 0

    for i in range(n):
        termino = y[i]
        for j in range(n):
            if j != i:
                termino *= (x_sym - x[j]) / (x[i] - x[j])
        polinomio += termino

        polinomioSimp = sp.nsimplify(polinomio,rational=True, tolerance= 1e-4)

    return sp.expand(polinomioSimp)

# Pedir al usuario las coordenadas
n = int(input("Introduce la cantidad de coordenadas: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Introduce x[{i}]: ")))
    y.append(float(input(f"Introduce y[{i}]: ")))

# Obtener el polinomio de Lagrange
polinomio_lagrange = interpolacion_lagrange(x, y)

print(f"El polinomio de Lagrange es: P(x) = {polinomio_lagrange}")


#Aquí empieza la gráfica
x_sym = sp.symbols('x')
polinomio_lambda = sp.lambdify(x_sym, polinomio_lagrange, 'numpy')

x_valores = np.linspace(min(x), max(x), 400)
y_valores = [polinomio_lambda(x_val) for x_val in x_valores]

# Aquí se grafica el polinomio de Lagrange
plt.figure()
plt.title("Polinomio de Lagrange")
plt.plot(x_valores, y_valores, color = 'red', label=f'P(x) = {polinomio_lagrange}')
plt.scatter(x, y, color='blue', label='Puntos propuestos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()