# system.py
# Este archivo define un sistema de ecuaciones diferenciales (EDs) que modela la interacción de sentimientos
# en una relación, utilizando el modelo de "amor" entre Romeo y Julieta.

import numpy as np  # Biblioteca para manejar operaciones numéricas y arreglos

def system_eq(a=-0.5, b=0.5):
    # Parámetros del modelo:
    # a: constante que representa la respuesta de Romeo hacia los sentimientos de Julieta
    # b: constante que representa la respuesta de Julieta hacia los sentimientos de Romeo

    # La función dydt representa el sistema de ecuaciones:
    # dy1/dt = a * y2 (respuesta de Romeo hacia Julieta)
    # dy2/dt = b * y1 (respuesta de Julieta hacia Romeo)
    # Aquí, y1 es el estado emocional de Romeo y y2 el de Julieta.

    def dydt(y):
        dy1dt = a * y[1]  # Derivada del estado de Romeo con respecto al tiempo
        dy2dt = b * y[0]  # Derivada del estado de Julieta con respecto al tiempo
        return np.array([dy1dt, dy2dt])

    # Envoltura que adapta dydt para recibir 2 argumentos, de modo que sea compatible con el formato esperado
    # en el módulo de simulación. Esta función "wrapped_dydt" convierte las entradas x y _ en el vector y necesario.
    def wrapped_dydt(x, _):
        y = np.array([x, _])  # Convierte x y _ en el vector y (formato adecuado para dydt)
        return dydt(y)  # Llama a la función interna dydt con el vector

    return wrapped_dydt
