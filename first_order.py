# first_order.py
# Este archivo define una ecuación diferencial (ED) de primer orden.
# La ED representa la resistencia al viento sobre un objeto en caída, dependiendo de su velocidad.

def first_order_eq():
    # Parámetros de la ecuación
    m = 70  # masa del objeto en kg
    g = 9.81  # aceleración debida a la gravedad en m/s^2
    k = 0.25  # constante de resistencia del aire en kg/m

    # Retorna una función lambda que representa la ecuación diferencial de primer orden
    # dv/dt = (mg - kv^2) / m, donde:
    # dv/dt es la tasa de cambio de la velocidad con respecto al tiempo,
    # v es la velocidad,
    # m es la masa del objeto,
    # g es la gravedad, y
    # k es la constante de resistencia del aire.
    return lambda v: (m * g - k * v**2) / m
