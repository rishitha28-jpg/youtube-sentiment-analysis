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

            # ⭐ VERY IMPORTANT DEBUG LINES
            print("STATUS CODE:", response.status_code)
            print("RAW RESPONSE:", response.text)

            result = response.json()

            label = result[0]["label"]
            score = result[0]["score"]

            sentiments.append({
                "label": label,
                "score": round(score * 100, 2)
            })

        except Exception as e:

            print("Sentiment error:", e)

            sentiments.append({
                "label": "NEUTRAL",
                "score": 0
            })

    return sentiments