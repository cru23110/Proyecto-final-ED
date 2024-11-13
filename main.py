# main.py
# Este archivo sirve como el punto de entrada principal para el proyecto de Simulación de Ecuaciones Diferenciales.
# Muestra un menú para que el usuario seleccione el tipo de ecuación diferencial (ED) que desea simular.
# Según la elección del usuario, importa y configura la función de ED adecuada y ejecuta la simulación.

import first_order  # Módulo para la Ecuación Diferencial de Primer Orden
import second_order  # Módulo para la Ecuación Diferencial de Segundo Orden
import system  # Módulo para el Sistema de Ecuaciones Diferenciales
from simulation import simulate  # Función principal de simulación que maneja los métodos de Euler y RK4


def main():
    # Muestra un menú para que el usuario elija el tipo de ED que desea simular
    print("Seleccione el tipo de ecuación diferencial:")
    print("1. ED de Primer Orden")
    print("2. ED de Segundo Orden")
    print("3. Sistema de EDs")
    # Obtiene la entrada del usuario y selecciona la función de ED adecuada según la opción elegida
    choice = input("Opción: ")

    if choice == "1":
        # ED de primer orden (ejemplo: resistencia al viento)
        eq_func = first_order.first_order_eq()
        eq_type = "first_order"
    elif choice == "2":
        # ED de segundo orden (ejemplo: oscilador armónico)
        eq_func = second_order.second_order_eq()
        eq_type = "second_order"
    elif choice == "3":
        # Sistema de EDs (ejemplo: modelo de amor de Romeo y Julieta)
        eq_func = system.system_eq()
        eq_type = "system"
    else:
        # Manejo de entrada inválida
        print("Opción no válida.")
        return

    # Parámetros de simulación
    t0, tf, h = 0, 10, 0.1  # Tiempo inicial, tiempo final, y tamaño del paso

    # Ejecuta la simulación con ambos métodos (Adams y RK4) automáticamente
    simulate(eq_func, t0, tf, h, eq_type)


# Verifica si el script se está ejecutando directamente (no importado como módulo) y llama a main()
if __name__ == "__main__":
    main()
