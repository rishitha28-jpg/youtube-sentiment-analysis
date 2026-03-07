from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(comments):

    comments = comments[:20]

    sentiments = []

    for comment in comments:

        score = analyzer.polarity_scores(comment)
        compound = score["compound"]

        if compound >= 0.05:
            sentiment = "POSITIVE"
        elif compound <= -0.05:
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"

        sentiments.append({
            "comment": comment,
            "sentiment": sentiment,
            "score": round(compound * 100, 2)
        })

    return sentiments