
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.core.config import settings


def get_youtube_comments(video_id: str, max_comments: int = 20):

    try:

        youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)

        comments = []
        next_page_token = None

        while len(comments) < max_comments:

            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=20,
                order="time",
                pageToken=next_page_token,
                textFormat="plainText"
            )

            response = request.execute()

            for item in response.get("items", []):

                comment = (
                    item["snippet"]
                    ["topLevelComment"]
                    ["snippet"]
                    .get("textDisplay", "")
                )

                if comment:
                    comments.append(comment)

                if len(comments) >= max_comments:
                    break

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        print(f"Fetched {len(comments)} comments")

        return comments

    except HttpError as e:
        print("YouTube API HTTP Error:", e)
        return []

    except Exception as e:
        print("YouTube API Error:", e)
        return []