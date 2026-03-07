# from transformers import pipeline

# # load model once
# sentiment_model = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def analyze_sentiments(comments):

#     results = sentiment_model(comments)

#     sentiments = []

#     for r in results:
#         sentiments.append({
#             "label": r["label"],
#             "score": round(r["score"] * 100, 2)
#         })

#     return sentiments
from transformers import pipeline

# load model once
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiments(comments):

    comments = comments[:20]   # limit comments for Render memory

    results = sentiment_model(comments)

    sentiments = []

    for r in results:
        sentiments.append({
            "label": r["label"],
            "score": round(r["score"] * 100, 2)
        })

    return sentiments