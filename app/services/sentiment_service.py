import requests
from app.core.config import settings

API_URL = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {settings.HF_API_TOKEN}",
    "Content-Type": "application/json"
}


def analyze_sentiments(comments):

    payload = {"inputs": comments}

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        sentiments = []

        for r in result:

            # HuggingFace returns list of predictions
            if isinstance(r, list):

                # choose highest score prediction
                r = max(r, key=lambda x: x["score"])

            label = r.get("label", "NEUTRAL")
            score = r.get("score", 0)

            sentiments.append((label, round(score * 100, 2)))

        return sentiments

    except Exception as e:
        print("Sentiment error:", e)
        return [("NEUTRAL", 0.0)] * len(comments)