from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(comments):

    comments = comments[:20]

    sentiments = []

    for comment in comments:

        score = analyzer.polarity_scores(comment)
        compound = score["compound"]

        if compound >= 0.05:
            label = "POSITIVE"
        elif compound <= -0.05:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        sentiments.append({
            "comment": comment,
            "label": label,   # ← IMPORTANT (not "sentiment")
            "score": round(compound * 100, 2)
        })

    return sentiments