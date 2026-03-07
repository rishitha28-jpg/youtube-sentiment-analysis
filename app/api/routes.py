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

        if not comments:
            raise HTTPException(
                status_code=404,
                detail="No comments found for this video"
            )

        print(f"Fetched {len(comments)} comments")

        # Batch sentiment analysis
        sentiments = analyze_sentiments(comments)

        print("Sentiment analysis completed")

        results = []

        for comment, (label, score) in zip(comments, sentiments):

            results.append(
                CommentSentiment(
                    comment=comment,
                    sentiment=label,
                    score=score
                )
            )

        return VideoSentimentResponse(
            video_id=video_id,
            results=results
        )

    except HTTPException:
        raise

    except Exception as e:
        print("API Error:", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")