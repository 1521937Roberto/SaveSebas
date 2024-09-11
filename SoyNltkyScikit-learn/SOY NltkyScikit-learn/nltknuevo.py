import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Descargar el conjunto de datos necesario para análisis de sentimientos
nltk.download('vader_lexicon')

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Lista de frases para analizar
frases = [
    "Me encanta este producto, es increíble!",
    "Este lugar es terrible, nunca volveré.",
    "Es un día normal, no tengo muchas opiniones al respecto.",
    "Estoy muy emocionado por este nuevo proyecto.",
    "Qué pésima atención al cliente, estoy muy decepcionado."
]

# Analizar el sentimiento de cada frase
for frase in frases:
    print(f"Frase: {frase}")
    sentimiento = sia.polarity_scores(frase)
    print(f"Análisis de Sentimiento: {sentimiento}")
    print("-" * 40)
