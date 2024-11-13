import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la ecuación de resistencia al viento
m = 70  # masa (kg)
g = 9.81  # gravedad (m/s^2)
k = 0.25  # constante de resistencia (kg/m)

# ED de primer orden: dv/dt = (mg - kv^2) / m
def dv_dt(v):
    return (m * g - k * v**2) / m

# Método de Euler
def euler_method(dv_dt, v0, t0, tf, h):
    t_values = np.arange(t0, tf, h)
    v_values = [v0]
    for t in t_values[:-1]:
        v = v_values[-1]
        v_next = v + h * dv_dt(v)
        v_values.append(v_next)
    return t_values, np.array(v_values)

# Método de Runge-Kutta de 4to orden (RK4)
def rk4_method(dv_dt, v0, t0, tf, h):
    t_values = np.arange(t0, tf, h)
    v_values = [v0]
    for t in t_values[:-1]:
        v = v_values[-1]
        k1 = dv_dt(v)
        k2 = dv_dt(v + h * k1 / 2)
        k3 = dv_dt(v + h * k2 / 2)
        k4 = dv_dt(v + h * k3)
        v_next = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        v_values.append(v_next)
    return t_values, np.array(v_values)

# Condiciones iniciales y tiempo de simulación
v0 = 0  # velocidad inicial (m/s)
t0, tf = 0, 10  # tiempo inicial y final (s)
h = 0.1  # tamaño del paso

# Soluciones numéricas
t_euler, v_euler = euler_method(dv_dt, v0, t0, tf, h)
t_rk4, v_rk4 = rk4_method(dv_dt, v0, t0, tf, h)

# Graficar resultados
plt.plot(t_euler, v_euler, label="Euler", linestyle="--")
plt.plot(t_rk4, v_rk4, label="RK4", linestyle="-")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.legend()
plt.title("Simulación de la resistencia al viento")
plt.show()
