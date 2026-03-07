from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load analyzer once
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(comments):

    comments = comments[:20]   # limit comments

    sentiments = []

    for comment in comments:

        score = analyzer.polarity_scores(comment)
        compound = score["compound"]

        # Recommended thresholds
        if compound >= 0.05:
            label = "POSITIVE"
        elif compound <= -0.05:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        sentiments.append({
            "comment": comment,
            "sentiment": label,
            "score": round(compound * 100, 2)
        })

    return sentiments