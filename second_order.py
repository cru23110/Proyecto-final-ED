# second_order.py
# Este archivo define una ecuación diferencial (ED) de segundo orden.
# La ED representa un oscilador armónico, como un sistema de resorte.

def second_order_eq(k=1.0, m=1.0):
    # Parámetros de la ecuación
    # k: constante de resorte (N/m)
    # m: masa del objeto (kg)

    # Retorna una función que calcula dx/dt y dv/dt en función de x y v.
    # Esta transformación permite tratar una ED de segundo orden como un sistema de dos EDs de primer orden.
    # La ecuación de segundo orden es: d²x/dt² = - (k/m) * x, donde:
    # dx/dt = v (velocidad)
    # dv/dt = -(k/m) * x (aceleración, según la ley de Hooke)

    def dx_dt(x, v):
        return v, -(k / m) * x  # Retorna la derivada de la posición y la derivada de la velocidad

    return dx_dt
