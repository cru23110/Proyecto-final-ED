# simulation.py
# Este archivo contiene los métodos numéricos (Euler y Runge-Kutta de cuarto orden) para resolver ecuaciones diferenciales (EDs).
# También incluye la función principal de simulación, que ejecuta ambos métodos y grafica los resultados para comparar precisión y estabilidad.

import numpy as np
import matplotlib.pyplot as plt

def adams_bashforth_method(dv_dt, initial_conditions, t0, tf, h, order=1):
    # Implementación del Método de Adams-Bashforth de cuarto orden.
    # Calcula los primeros tres valores con RK4 antes de usar Adams-Bashforth, ya que este método es de múltiples pasos.

    # Inicialización de valores de tiempo
    t_values = np.arange(t0, tf, h)
    results = [initial_conditions]

    # Calcular los primeros tres valores usando el método RK4
    for i in range(3):
        if order == 1:
            v = results[-1]
            k1 = dv_dt(v)
            k2 = dv_dt(v + h * k1 / 2)
            k3 = dv_dt(v + h * k2 / 2)
            k4 = dv_dt(v + h * k3)
            v_next = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            results.append(v_next)
        elif order == 2:
            x, v = results[-1]
            dx1, dv1 = dv_dt(x, v)
            dx2, dv2 = dv_dt(x + h * dx1 / 2, v + h * dv1 / 2)
            dx3, dv3 = dv_dt(x + h * dx2 / 2, v + h * dv2 / 2)
            dx4, dv4 = dv_dt(x + h * dx3, v + h * dv3)
            x_next = x + (h / 6) * (dx1 + 2 * dx2 + 2 * dx3 + dx4)
            v_next = v + (h / 6) * (dv1 + 2 * dv2 + 2 * dv3 + dv4)
            results.append((x_next, v_next))

    # Método de Adams-Bashforth de cuarto orden
    for i in range(3, len(t_values) - 1):
        if order == 1:
            # Valores de f en los últimos cuatro puntos
            f_n = dv_dt(results[-1])
            f_n1 = dv_dt(results[-2])
            f_n2 = dv_dt(results[-3])
            f_n3 = dv_dt(results[-4])

            # Fórmula de Adams-Bashforth de cuarto orden para el siguiente valor
            v_next = results[-1] + h * (55 * f_n - 59 * f_n1 + 37 * f_n2 - 9 * f_n3) / 24
            results.append(v_next)
        elif order == 2:
            # Valores de f en los últimos cuatro puntos para sistemas
            x_n, v_n = results[-1]
            x_n1, v_n1 = results[-2]
            x_n2, v_n2 = results[-3]
            x_n3, v_n3 = results[-4]

            dx_n, dv_n = dv_dt(x_n, v_n)
            dx_n1, dv_n1 = dv_dt(x_n1, v_n1)
            dx_n2, dv_n2 = dv_dt(x_n2, v_n2)
            dx_n3, dv_n3 = dv_dt(x_n3, v_n3)

            # Fórmula de Adams-Bashforth para el siguiente paso de x y v
            x_next = x_n + h * (55 * dx_n - 59 * dx_n1 + 37 * dx_n2 - 9 * dx_n3) / 24
            v_next = v_n + h * (55 * dv_n - 59 * dv_n1 + 37 * dv_n2 - 9 * dv_n3) / 24
            results.append((x_next, v_next))

    return t_values, np.array(results)

def rk4_method(dv_dt, initial_conditions, t0, tf, h, order=1):
    # Método de Runge-Kutta de 4º Orden (RK4) para mayor precisión.

    t_values = np.arange(t0, tf, h)
    results = [initial_conditions]

    for t in t_values[:-1]:
        if order == 1:
            v = results[-1]
            k1 = dv_dt(v)
            k2 = dv_dt(v + h * k1 / 2)
            k3 = dv_dt(v + h * k2 / 2)
            k4 = dv_dt(v + h * k3)
            v_next = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            results.append(v_next)
        elif order == 2:
            x, v = results[-1]
            dx1, dv1 = dv_dt(x, v)
            dx2, dv2 = dv_dt(x + h * dx1 / 2, v + h * dv1 / 2)
            dx3, dv3 = dv_dt(x + h * dx2 / 2, v + h * dv2 / 2)
            dx4, dv4 = dv_dt(x + h * dx3, v + h * dv3)
            x_next = x + (h / 6) * (dx1 + 2 * dx2 + 2 * dx3 + dx4)
            v_next = v + (h / 6) * (dv1 + 2 * dv2 + 2 * dv3 + dv4)
            results.append((x_next, v_next))

    return t_values, np.array(results)

def simulate(dv_dt, t0=0, tf=10, h=0.1, eq_type="first_order"):
    # Función principal de simulación que ejecuta ambos métodos (Adams-Bashforth y RK4) y grafica los resultados.

    # Condiciones iniciales según el tipo de ED
    if eq_type == "first_order":
        initial_conditions = 0
    elif eq_type == "second_order":
        initial_conditions = (1, 0)
    elif eq_type == "system":
        initial_conditions = np.array([1, 1])

    # Ejecuta el método de Adams-Bashforth
    t_adams, results_adams = adams_bashforth_method(dv_dt, initial_conditions, t0, tf, h,
                                                    order=(1 if eq_type == "first_order" else 2))

    # Ejecuta el método de Runge-Kutta de 4º Orden (RK4)
    t_rk4, results_rk4 = rk4_method(dv_dt, initial_conditions, t0, tf, h, order=(1 if eq_type == "first_order" else 2))

    # Calcular el Error Cuadrático Medio (MSE) entre los resultados de Adams-Bashforth y RK4
    mse = np.mean((results_adams - results_rk4) ** 2)
    print(f"Error cuadrático medio (MSE) entre Adams-Bashforth y RK4: {mse}")

    # Grafica los resultados para comparar ambos métodos
    plt.plot(t_adams, results_adams[:, 0] if eq_type != "first_order" else results_adams, label="Adams-Bashforth", linestyle="--")
    plt.plot(t_rk4, results_rk4[:, 0] if eq_type != "first_order" else results_rk4, label="RK4", linestyle="-")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor")
    plt.legend()
    plt.title(f"Simulación de {eq_type} con Adams-Bashforth y RK4")
    plt.show()