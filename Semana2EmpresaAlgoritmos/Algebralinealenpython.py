import numpy as np

# Matriz de horas de disponibilidad de los instructores por tipo de servicio
horas_instructores = np.array([
    [10, 5, 8],   # Instructor 1: (Programas Académicos, Opciones Ocupacionales, Lecciones de Conducción)
    [15, 10, 5],  # Instructor 2
    [5, 12, 10]   # Instructor 3
])

# Calculamos el total de horas sumando las columnas
horas_totales = np.sum(horas_instructores, axis=0)

# Mostramos los resultados
servicios = ['Programas Académicos', 'Opciones Ocupacionales', 'Lecciones de Conducción']
for i, servicio in enumerate(servicios):
    print(f"Total de horas para {servicio}: {horas_totales[i]} horas por semana")
