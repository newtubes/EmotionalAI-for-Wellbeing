# EmotionalAI-for-Wellbeing
Este módulo de Python demuestra cómo se puede analizar el sentimiento de texto (como entradas de un diario personal) para una aplicación de bienestar como 'Siempre es Hoy'
# SiempreEsHoy-EmotionalAI-Module ✨

Un módulo de Procesamiento de Lenguaje Natural (NLP) diseñado para analizar el sentimiento y las emociones en texto, concebido como el corazón inteligente de la aplicación de bienestar "Siempre es Hoy". Este proyecto es una demostración de cómo la Inteligencia Artificial puede fusionarse con la intuición humana para ofrecer experiencias personalizadas que nutren el alma.

---

## 💡 Propósito

En el camino de transformar la vida en arte, "Siempre es Hoy" busca ser un espacio digital donde el bienestar, la creatividad y la tecnología se unan. Este módulo de IA es un primer paso fundamental hacia esa visión. Su objetivo principal es:

* **Analizar el tono emocional** de las entradas de texto del usuario (como un diario de gratitud o reflexiones).
* Proveer una base para un **sistema de recomendación inteligente** que sugiera contenido personalizado (meditaciones, piezas de arte, música, prompts creativos) basado en el estado emocional detectado.

Este proyecto independiente muestra mis habilidades en NLP y mi enfoque en construir soluciones tecnológicas con un profundo impacto humano.

---

## 🚀 Cómo Funciona (en esta fase)

El módulo utiliza librerías de Python para procesar cadenas de texto y determinar su polaridad sentimental (positivo, negativo, neutral) o emociones más específicas (ej. alegría, tristeza, calma).

1.  **Entrada de Texto:** Recibe una cadena de texto (simulando la entrada del usuario en un diario de la app).
2.  **Análisis de Sentimiento/Emoción:** Aplica modelos pre-entrenados para clasificar el sentimiento o detectar emociones clave.
3.  **Salida:** Devuelve el sentimiento/emoción detectado, que luego podría ser utilizado por la aplicación principal para personalizar la experiencia del usuario.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x:** Lenguaje principal de desarrollo.
* **TextBlob y NLTK:** Para el análisis de sentimiento inicial.
* **Pandas, matplotlib

## Estructura propuesta para el modulo

SiempreEsHoy-EmotionalAI-Module/
│
├── emotion_analyzer/          # Carpeta principal del módulo
│   ├── __init__.py
│   ├── sentiment.py           # Análisis básico con TextBlob
│   ├── emotions.py            # Análisis avanzado con NLTK/VADER
│   └── utils.py               # Funciones auxiliares (limpieza de texto, etc.)
│
├── tests/                     # Pruebas unitarias
│   └── test_analyzer.py
│
├── main.py                    # Ejemplo de uso interactivo
└── requirements.txt           # Dependencias (TextBlob, NLTK, etc.)

## ⚙️ Configuración y Ejecución

Para ejecutar este módulo en tu entorno local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TuUsuarioDeGitHub/SiempreEsHoy-EmotionalAI-Module.git](https://github.com/TuUsuarioDeGitHub/SiempreEsHoy-EmotionalAI-Module.git)
    cd SiempreEsHoy-EmotionalAI-Module
    ```
2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install [nombre-de-libreria-1] [nombre-de-libreria-2] # ej. pip install textblob nltk
    # Si usas NLTK por primera vez, es posible que necesites descargar sus datos:
    # python -m nltk.downloader punkt averaged_perceptron_tagger vader_lexicon
    ```
4.  **Ejecuta el script de ejemplo:**
    ```bash
    python main_sentiment_analyzer.py # O el nombre que le des a tu script principal
    ```
    (Incluye un pequeño ejemplo de código en tu `main_sentiment_analyzer.py` que demuestre su funcionamiento con un texto de prueba).

---

## 📝 Ejemplos de Uso (en tu script Python o un Jupyter Notebook)

```python
# Importa tu función de análisis de sentimiento
from sentiment_analyzer import analyze_text_sentiment # Asumiendo que pones la lógica en un archivo llamado sentiment_analyzer.py

text1 = "Hoy me siento increíblemente inspirada y agradecida por las nuevas ideas. El futuro es brillante."
text2 = "A veces, las cosas se sienten un poco pesadas, pero sé que estoy aprendiendo y creciendo."
text3 = "Este día es perfecto, la música resuena con mi alma."

print(f"Texto 1: '{text1}' -> Sentimiento: {analyze_text_sentiment(text1)}")
print(f"Texto 2: '{text2}' -> Sentimiento: {analyze_text_sentiment(text2)}")
print(f"Texto 3: '{text3}' -> Sentimiento: {analyze_text_sentiment(text3)}")


```mermaid
graph TD
    A[Texto de Usuario] --> B(Análisis con TextBlob)
    A --> C(Análisis con NLTK/VADER)
    B --> D[Resultado: Polaridad/Subjetividad]
    C --> E[Resultado: Emociones Detalladas]
    D & E --> F[Recomendación Personalizada]
