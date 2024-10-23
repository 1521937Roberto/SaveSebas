# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuración del estilo de los gráficos
sns.set(style="whitegrid")

# Generar notas aleatorias para los turnos (notas entre 0 y 20)
np.random.seed(42)

# Notas para el turno mañana (30 estudiantes)
notas_mañana = np.random.randint(10, 21, size=30)

# Notas para el turno tarde (55 estudiantes)
notas_tarde = np.random.randint(8, 21, size=55)

# Crear un DataFrame para manejar los datos
data = {
    'Turno': ['Mañana'] * 30 + ['Tarde'] * 55,
    'Notas': np.concatenate([notas_mañana, notas_tarde])
}

df = pd.DataFrame(data)

# Estadísticas descriptivas para ambos turnos
print("Estadísticas descriptivas para el turno mañana:")
print(df[df['Turno'] == 'Mañana']['Notas'].describe())
print("\nEstadísticas descriptivas para el turno tarde:")
print(df[df['Turno'] == 'Tarde']['Notas'].describe())

# Calcular la moda para ambos turnos de manera correcta
moda_mañana = stats.mode(df[df['Turno'] == 'Mañana']['Notas'], keepdims=True).mode[0]
moda_tarde = stats.mode(df[df['Turno'] == 'Tarde']['Notas'], keepdims=True).mode[0]

print(f"\nModa de las notas (Mañana): {moda_mañana}")
print(f"Moda de las notas (Tarde): {moda_tarde}")

# -------- Gráficos ---------

# 1. Histograma de la distribución de notas para ambos turnos
plt.figure(figsize=(10, 6))
sns.histplot(df, x='Notas', hue='Turno', multiple='stack', bins=10, palette='Set2')
plt.title('Distribución de Notas por Turno (Mañana y Tarde)', fontsize=14)
plt.xlabel('Notas')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(True)
plt.show()

# 2. Boxplot para visualizar la dispersión de las notas por turno
plt.figure(figsize=(8, 6))
sns.boxplot(x='Turno', y='Notas', data=df, palette='Set3')
plt.title('Boxplot de las Notas por Turno', fontsize=14)
plt.ylabel('Notas')
plt.grid(True)
plt.show()

# 3. Gráfico de barras de la media de notas por turno
media_mañana = df[df['Turno'] == 'Mañana']['Notas'].mean()
media_tarde = df[df['Turno'] == 'Tarde']['Notas'].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=['Mañana', 'Tarde'], y=[media_mañana, media_tarde], palette='coolwarm')
plt.title('Media de Notas por Turno', fontsize=14)
plt.ylabel('Media de Notas')
plt.grid(True)
plt.show()
