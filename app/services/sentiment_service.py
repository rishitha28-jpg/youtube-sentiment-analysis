import requests
from app.core.config import settings

# Official HuggingFace inference endpoint
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {settings.HF_API_TOKEN}"
}


def analyze_sentiments(comments):

    sentiments = []

    for comment in comments:

        payload = {
            "inputs": comment
        }

        try:

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=30
            )

            result = response.json()

            # Debug print
            print("HF response:", result)

            if isinstance(result, list):
                result = result[0]

            label = result.get("label", "NEUTRAL")
            score = result.get("score", 0)

            sentiments.append((label, round(score * 100, 2)))

        except Exception as e:
            print("Sentiment error:", e)
            sentiments.append(("NEUTRAL", 0))

    return sentiments