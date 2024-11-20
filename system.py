# system.py
# Este archivo define un sistema de ecuaciones diferenciales (EDs) basado en un modelo generalizado de interacción.
# utilizando el modelo de "amor" entre Romeo y Julieta.

import numpy as np  # Biblioteca para manejar operaciones numéricas y arreglos

def system_eq(a=1.0, b=1.0, c=1.0, d=1.0):
    # Parámetros del modelo:
    # a, b, c, d: coeficientes que representan las interacciones entre x(t) e y(t)

    # La función dydt representa el sistema de ecuaciones:
    # dx/dt = a * x + b * y
    # dy/dt = c * x + d * y
    def dydt(y):
        dxdt = a * y[0] + b * y[1]
        dydt = c * y[0] + d * y[1]
        return np.array([dxdt, dydt])

    # Envoltura que adapta dydt para recibir 2 argumentos (x y _) en lugar de un vector.
    # Esto es necesario si el módulo de simulación espera que las funciones manejen x y _ de forma separada.
    def wrapped_dydt(x, _):
        y = np.array([x, _])  # Convierte x y _ en el vector y necesario
        return dydt(y)  # Llama a la función interna dydt con el vector

    return wrapped_dydt
