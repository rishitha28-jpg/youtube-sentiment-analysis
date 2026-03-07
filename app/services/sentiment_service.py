import requests
from app.core.config import settings

API_URL = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {settings.HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def analyze_sentiments(comments):

    sentiments = []

    for comment in comments:

        try:

            payload = {"inputs": comment}

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload
            )

            result = response.json()

            # HuggingFace returns list of labels
            best = max(result, key=lambda x: x["score"])

            sentiments.append({
                "label": best["label"],
                "score": round(best["score"] * 100, 2)
            })

        except Exception as e:

            print("Sentiment error:", e)

            sentiments.append({
                "label": "NEUTRAL",
                "score": 0
            })

    return sentiments