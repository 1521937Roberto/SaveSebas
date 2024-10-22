import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Hiperparámetros
batch_size = 64
learning_rate = 0.01
epochs = 5

# Transformación para normalizar las imágenes de entrada
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Descargar el dataset MNIST (números manuscritos)
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# Definir la red neuronal
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 512)  # Capa totalmente conectada
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)       # 10 clases de salida (dígitos del 0 al 9)

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # Aplanar las imágenes (28x28 píxeles)
        x = F.relu(self.fc1(x))  # Función de activación ReLU
        x = F.relu(self.fc2(x))
        x = self.fc3(x)          # No aplicamos ReLU en la última capa
        return x

# Inicializar el modelo, el optimizador y la función de pérdida
model = NeuralNet()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss()

# Función para entrenar el modelo
def train():
    model.train()
    for epoch in range(epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            # Hacer las predicciones
            output = model(data)
            # Calcular la pérdida
            loss = criterion(output, target)
            # Hacer el paso hacia atrás (backpropagation) y actualizar los pesos
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch_idx % 100 == 0:
                print(f'Epoch {epoch+1}/{epochs} | Batch {batch_idx} | Loss: {loss.item():.4f}')

# Función para evaluar el modelo
def test():
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    print(f'Accuracy: {100 * correct / total:.2f}%')

if __name__ == '__main__':
    print("Entrenando el modelo...")
    train()
    print("Evaluando el modelo...")
    test()
