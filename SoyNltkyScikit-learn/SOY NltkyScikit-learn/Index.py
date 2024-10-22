# Importamos todas las bibliotecas necesarias
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar el conjunto de datos de dígitos
digits = load_digits()

# 2. Mostrar detalles del conjunto de datos
print(f"Datos de características (shape): {digits.data.shape}")  # 1797 imágenes con 64 características
print(f"Ejemplo de etiquetas (números): {digits.target[:10]}")  # Primeros 10 números

# 3. Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# 4. Crear un modelo de Regresión Logística
model = LogisticRegression(max_iter=10000)

# 5. Entrenar el modelo
model.fit(X_train, y_train)

# 6. Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# 7. Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPrecisión del modelo: {accuracy * 100:.2f}%")

# 8. Mostrar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de confusión:")
print(conf_matrix)

# 9. Mostrar un reporte de clasificación más detallado
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# 10. Visualizar algunas predicciones incorrectas
# Encontrar índices de predicciones incorrectas
misclassified_indexes = np.where(y_pred != y_test)[0]

# Mostrar algunas imágenes mal clasificadas
plt.figure(figsize=(10, 5))
for i, index in enumerate(misclassified_indexes[:5]):
    plt.subplot(1, 5, i + 1)
    plt.imshow(digits.images[index], cmap="gray")
    plt.title(f"Pred: {y_pred[index]}\nTrue: {y_test[index]}")
    plt.axis("off")
plt.show()
