import requests
from app.core.config import settings

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {settings.HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def analyze_sentiments(comments):

    # ⭐ IMPORTANT DEBUG LINE
    print("HF TOKEN:", settings.HF_API_TOKEN)

    sentiments = []

    for comment in comments:

        try:

            payload = {"inputs": comment}

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=20
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            if response.status_code != 200:
                sentiments.append({
                    "label": "NEUTRAL",
                    "score": 0
                })
                continue

            result = response.json()

            if isinstance(result, dict) and "error" in result:
                print("HF API Error:", result["error"])
                sentiments.append({
                    "label": "NEUTRAL",
                    "score": 0
                })
                continue

            best = max(result, key=lambda x: x["score"])

            sentiments.append({
                "label": best["label"],
                "score": round(best["score"] * 100, 2)
            })

        except Exception as e:

            print("Sentiment error:", str(e))

            sentiments.append({
                "label": "NEUTRAL",
                "score": 0
            })

    return sentiments