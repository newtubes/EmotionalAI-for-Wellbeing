from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """Analiza polaridad y subjetividad con TextBlob."""
    analysis = TextBlob(text)
    return {
        "polarity": analysis.sentiment.polarity,
        "subjectivity": analysis.sentiment.subjectivity,
        "assessment": "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
    }