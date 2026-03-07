
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# load analyzer once
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(comments):

    comments = comments[:20]   # limit comments for safety

    sentiments = []

    for comment in comments:

        score = analyzer.polarity_scores(comment)

        if score["compound"] >= 0.05:
            label = "POSITIVE"
        elif score["compound"] <= -0.05:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        sentiments.append({
            "label": label,
            "score": round(score["compound"] * 100, 2)
        })

    return sentiments