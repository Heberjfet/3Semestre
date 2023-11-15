import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from sympy.plotting import plot

def metodo1():
    A, B = sp.symbols('a b')
    while True:
        try:
            func = input("Ingrese la diferencial en términos de A, B: ")
            function = sp.sympify(func)
            break
        except ValueError:
            pass
    f = sp.lambdify((A, B), function)
    a_0 = float(input("Ingrese el valor de a_0: "))
    b_0 = float(input("Ingrese el valor de b_0: "))
    a_f = float(input("Ingrese el valor de a_f: "))
    n = int(input("Ingrese el número de intervalos: "))
    h = (a_f - a_0) / n
    print(h)
    b_i = 0  # Cambié yi a b_i
    print("||   A  ||    B    ||   f(a,b)   ||")
    for i in range(n + 1):
        print("|| "+"{:.2f}".format(a_0)+" ||  "+"{:.3f}".format(b_0)+"  ||    "+"{:.3f}".format(f(a_0, b_0))+"   ||")
        b_i = (b_0 + (h * f(a_0, b_0)))
        a_0 += h
        b_0 = b_i

def metodo2():
    X = sp.Symbol("x")
    while True:
        try:
            func_input = input("Ingrese la función en términos de X: ")
            function = sp.sympify(func_input)
            break
        except ValueError:  # Corregí la sangría aquí
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


def metodo3():
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

def switch_case(value):
    return {
        'metodo1': metodo1,
        'metodo2': metodo2,
        'metodo3': metodo3,
    }.get(value, lambda: 'Invalid case')()

# Test the function
print(switch_case('metodo1'))
print(switch_case('metodo4'))

