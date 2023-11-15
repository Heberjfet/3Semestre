import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt

def factorial(var):
    if var == 0:
        return 1
    else:
        return var * factorial(var - 1)

X = sp.Symbol("x")
while True:
    try:
        func_input = input("Ingrese la función en términos de X: ")
        function = sp.sympify(func_input)
        break
    except ValueError:
        pass

x0 = float(input("Ingrese el valor de X0: "))
evaluations = []
derivative = func_input
series = 0
i = 0

while True:
    if derivative == 0:
        break
    else:
        f = sp.lambdify(X, derivative)
        evaluations.append(f(x0))
        derivative = sp.diff(function, X)
        function = derivative

    series += (evaluations[i] / factorial(i)) * (X - x0) ** i
    i += 1

print(f"La serie resultante es: {series}")

graph = plot(series, show=False)
graph.title = "Gráfica"
graph.xlabel = "X"
graph.ylabel = "Y"
graph.show()
