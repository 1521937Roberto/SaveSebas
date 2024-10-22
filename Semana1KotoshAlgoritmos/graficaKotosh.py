import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Datos históricos de campañas anteriores
data = {
    'tripticos': [500, 600, 400, 550, 450],
    'carteles': [1000, 1200, 800, 900, 950],
    'video': [2000, 2500, 1800, 2300, 2100],
    'redes_sociales': [1500, 1800, 1300, 1600, 1700],
    'ventas': [25000, 30000, 22000, 28000, 27000]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Separar las variables independientes (gastos publicitarios) y la variable dependiente (ventas)
X = df[['tripticos', 'carteles', 'video', 'redes_sociales']]
y = df['ventas']

# Dividir los datos en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal múltiple
modelo = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Realizar predicciones con el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R^2): {r2}")

# Obtener los coeficientes del modelo
coeficientes = modelo.coef_
print("\nCoeficientes del modelo:")
print(f"Trípticos: {coeficientes[0]}")
print(f"Carteles: {coeficientes[1]}")
print(f"Video: {coeficientes[2]}")
print(f"Redes Sociales: {coeficientes[3]}")

# Optimización: calcular la mejor combinación para maximizar ventas
# Supongamos que tienes un presupuesto total de 6000 soles y quieres distribuirlo de manera óptima

presupuesto_total = 6000

# Según los coeficientes, distribuimos el presupuesto en las diferentes áreas
gasto_tripticos_optimo = (coeficientes[0] / sum(coeficientes)) * presupuesto_total
gasto_carteles_optimo = (coeficientes[1] / sum(coeficientes)) * presupuesto_total
gasto_video_optimo = (coeficientes[2] / sum(coeficientes)) * presupuesto_total
gasto_redes_sociales_optimo = (coeficientes[3] / sum(coeficientes)) * presupuesto_total

# Mostrar el resultado
print(f"\nDistribución óptima del presupuesto (Total: {presupuesto_total} soles):")
print(f"Gasto óptimo en trípticos: {gasto_tripticos_optimo:.2f} soles")
print(f"Gasto óptimo en carteles: {gasto_carteles_optimo:.2f} soles")
print(f"Gasto óptimo en video promocional: {gasto_video_optimo:.2f} soles")
print(f"Gasto óptimo en redes sociales: {gasto_redes_sociales_optimo:.2f} soles")

# Graficar los gastos históricos
plt.figure(figsize=(10, 5))
plt.bar(['Trípticos', 'Carteles', 'Video', 'Redes Sociales'], df[['tripticos', 'carteles', 'video', 'redes_sociales']].sum(), color='blue')
plt.title('Gastos Históricos en Publicidad de CETPRO KOTOSH')
plt.ylabel('Gasto Total (S/)')
plt.xlabel('Tipos de Publicidad')
plt.grid(axis='y')
plt.show()

# Graficar la distribución óptima del presupuesto
optimo_gastos = [gasto_tripticos_optimo, gasto_carteles_optimo, gasto_video_optimo, gasto_redes_sociales_optimo]
tipos_publicidad = ['Trípticos', 'Carteles', 'Video', 'Redes Sociales']

plt.figure(figsize=(10, 5))
plt.bar(tipos_publicidad, optimo_gastos, color='green')
plt.title('Distribución Óptima del Presupuesto de Publicidad')
plt.ylabel('Gasto Óptimo (S/)')
plt.xlabel('Tipos de Publicidad')
plt.grid(axis='y')
plt.show()
