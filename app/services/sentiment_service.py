# # from transformers import pipeline

# # # load model once
# # sentiment_model = pipeline(
# #     "sentiment-analysis",
# #     model="distilbert-base-uncased-finetuned-sst-2-english"
# # )

# # def analyze_sentiments(comments):

# #     results = sentiment_model(comments)

# #     sentiments = []

# #     for r in results:
# #         sentiments.append({
# #             "label": r["label"],
# #             "score": round(r["score"] * 100, 2)
# #         })

# #     return sentiments
# from transformers import pipeline

# # load model once
# sentiment_model = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english",
#     device=-1
# )

# def analyze_sentiments(comments):

#     comments = comments[:20]   # limit comments for Render memory

#     results = sentiment_model(comments)

#     sentiments = []

#     for r in results:
#         sentiments.append({
#             "label": r["label"],
#             "score": round(r["score"] * 100, 2)
#         })

#     return sentiments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(comments):

    comments = comments[:20]

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