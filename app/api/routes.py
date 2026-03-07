from fastapi import APIRouter, HTTPException
from app.services.youtube_service import get_youtube_comments
from app.services.sentiment_service import analyze_sentiments
from app.models.schemas import CommentSentiment, VideoSentimentResponse

router = APIRouter()


@router.get("/analyze/{video_id}", response_model=VideoSentimentResponse)
def analyze_video(video_id: str):

    try:

        print("Fetching comments from YouTube...")

        comments = get_youtube_comments(video_id)

        # Remove empty comments
        comments = [c for c in comments if c.strip() != ""]

        if not comments:
            raise HTTPException(
                status_code=404,
                detail="No comments found for this video"
            )

        print(f"Fetched {len(comments)} comments")

        # Run sentiment analysis
        sentiments = analyze_sentiments(comments)

        print("Sentiment analysis completed")

        results = []
        positive = 0
        negative = 0

        for comment, sentiment in zip(comments, sentiments):

            label = sentiment["label"]
            score = sentiment["score"]

            if label == "POSITIVE":
                positive += 1
            elif label == "NEGATIVE":
                negative += 1

            results.append(
                CommentSentiment(
                    comment=comment,
                    sentiment=label,
                    score=score
                )
            )

        # Calculate overall sentiment
        if positive > negative:
            overall = "POSITIVE"
        elif negative > positive:
            overall = "NEGATIVE"
        else:
            overall = "NEUTRAL"

        return VideoSentimentResponse(
            video_id=video_id,
            overall_sentiment=overall,
            positive_comments=positive,
            negative_comments=negative,
            results=results
        )

    except HTTPException:
        raise

    except Exception as e:
        print("API Error:", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")