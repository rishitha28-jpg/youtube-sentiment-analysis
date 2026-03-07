from pydantic import BaseModel
from typing import List

class CommentSentiment(BaseModel):
    comment: str
    sentiment: str
    score: float


class VideoSentimentResponse(BaseModel):
    video_id: str
    results: List[CommentSentiment]