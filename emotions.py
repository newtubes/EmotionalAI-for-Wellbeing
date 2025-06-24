from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_emotions(text: str) -> dict:
    """Detecta emociones con VADER (NLTK)."""
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return {
        "compound": scores["compound"],
        "emotions": {
            "positive": scores["pos"],
            "negative": scores["neg"],
            "neutral": scores["neu"]
        }
    }