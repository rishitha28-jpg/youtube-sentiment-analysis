# import requests
# from app.core.config import settings

# API_URL = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"

# headers = {
#     "Authorization": f"Bearer {settings.HF_API_TOKEN}",
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# def analyze_sentiments(comments):

#     sentiments = []

#     for comment in comments:

#         try:
#             payload = {"inputs": comment}

#             response = requests.post(
#                 API_URL,
#                 headers=headers,
#                 json=payload,
#                 timeout=30
#             )

#             print("STATUS:", response.status_code)
#             print("RAW:", response.text)

#             if response.status_code != 200:
#                 sentiments.append({"label": "NEUTRAL", "score": 0})
#                 continue

#             result = response.json()

#             # Router usually returns [[{label,score},...]]
#             if isinstance(result, list) and isinstance(result[0], list):
#                 predictions = result[0]
#             else:
#                 predictions = result

#             best = max(predictions, key=lambda x: x["score"])

#             sentiments.append({
#                 "label": best["label"],
#                 "score": round(best["score"] * 100, 2)
#             })

#         except Exception as e:
#             print("Sentiment error:", e)
#             sentiments.append({"label": "NEUTRAL", "score": 0})

#     return sentiments
from transformers import pipeline

# load model once
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiments(comments):

    results = sentiment_model(comments)

    sentiments = []

    for r in results:
        sentiments.append({
            "label": r["label"],
            "score": round(r["score"] * 100, 2)
        })

    return sentiments