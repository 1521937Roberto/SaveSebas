import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del péndulo
g = 9.81  # Aceleración gravitatoria (m/s^2)
L = 1.0   # Longitud del péndulo (m)
theta0 = np.pi / 4  # Ángulo inicial (45 grados)
omega0 = 0.0        # Velocidad angular inicial (rad/s)

# Ecuación diferencial del péndulo simple
def pendulo(t, y):
    theta, omega = y
    dydt = [omega, - (g / L) * np.sin(theta)]
    return dydt

# Intervalo de tiempo para la simulación
t_span = (0, 10)  # 10 segundos
t_eval = np.linspace(0, 10, 500)  # 500 puntos de evaluación

# Condiciones iniciales: [ángulo inicial, velocidad angular inicial]
y0 = [theta0, omega0]

# Resolver la ecuación diferencial
sol = solve_ivp(pendulo, t_span, y0, t_eval=t_eval)

# Extraer ángulos y tiempos
theta_sol = sol.y[0]  # Solución de los ángulos

# Graficar la solución
plt.figure(figsize=(10, 6))
plt.plot(sol.t, theta_sol, label='Ángulo del péndulo (θ)')
plt.title('Simulación del Movimiento de un Péndulo Simple')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.grid(True)
plt.legend()
plt.show()

