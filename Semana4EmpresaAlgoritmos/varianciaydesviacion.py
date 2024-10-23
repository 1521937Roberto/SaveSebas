# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración del estilo de los gráficos
sns.set(style="whitegrid")

# Notas para el turno mañana (30 estudiantes) y turno tarde (55 estudiantes)
np.random.seed(42)  # Para reproducibilidad
notas_mañana = np.random.randint(10, 21, size=30)  # Notas aleatorias entre 10 y 20
notas_tarde = np.random.randint(8, 21, size=55)    # Notas aleatorias entre 8 y 20

# Crear un DataFrame para manejar los datos
data = {
    'Turno': ['Mañana'] * 30 + ['Tarde'] * 55,
    'Notas': np.concatenate([notas_mañana, notas_tarde])
}

df = pd.DataFrame(data)

# Calcular varianza y desviación estándar
var_mañana = df[df['Turno'] == 'Mañana']['Notas'].var()
std_mañana = df[df['Turno'] == 'Mañana']['Notas'].std()
var_tarde = df[df['Turno'] == 'Tarde']['Notas'].var()
std_tarde = df[df['Turno'] == 'Tarde']['Notas'].std()

# Imprimir los resultados
print(f"Varianza (Mañana): {var_mañana:.2f}")
print(f"Desviación Estándar (Mañana): {std_mañana:.2f}")
print(f"Varianza (Tarde): {var_tarde:.2f}")
print(f"Desviación Estándar (Tarde): {std_tarde:.2f}")

# -------- Gráficos ---------

# 1. Histograma de las notas
plt.figure(figsize=(10, 6))
sns.histplot(df, x='Notas', hue='Turno', multiple='stack', bins=10, palette='Set2')
plt.title('Distribución de Notas por Turno (Mañana y Tarde)', fontsize=14)
plt.xlabel('Notas')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(True)
plt.axvline(df[df['Turno'] == 'Mañana']['Notas'].mean(), color='blue', linestyle='dashed', linewidth=1, label='Media Mañana')
plt.axvline(df[df['Turno'] == 'Tarde']['Notas'].mean(), color='orange', linestyle='dashed', linewidth=1, label='Media Tarde')
plt.legend()
plt.show()

# 2. Gráfico de barras de varianza y desviación estándar
labels = ['Mañana', 'Tarde']
var_values = [var_mañana, var_tarde]
std_values = [std_mañana, std_tarde]

x = np.arange(len(labels))  # la ubicación de las etiquetas
width = 0.35  # el ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, var_values, width, label='Varianza', color='skyblue')
rects2 = ax.bar(x + width/2, std_values, width, label='Desviación Estándar', color='salmon')

# Añadir algunas etiquetas
ax.set_ylabel('Valores')
ax.set_title('Varianza y Desviación Estándar por Turno')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Añadir etiquetas de valor a las barras
def autolabel(rects):
    """Adjuntar una etiqueta a cada barra."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(round(height, 2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 puntos verticales de offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.grid(axis='y', linestyle='--')
plt.show()
