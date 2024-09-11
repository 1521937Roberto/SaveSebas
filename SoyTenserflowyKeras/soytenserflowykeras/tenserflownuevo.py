import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesar los datos
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalización

# Construir el modelo
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Convertir las imágenes 28x28 en un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Capa densa con 128 neuronas y ReLU como función de activación
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por cada clase) y softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Graficar la precisión y la pérdida durante el entrenamiento
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
