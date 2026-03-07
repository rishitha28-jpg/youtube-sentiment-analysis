# from googleapiclient.discovery import build
# from app.core.config import settings


# def get_youtube_comments(video_id: str, max_comments: int = 200):

#     youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)

#     comments = []
#     next_page_token = None

#     while True:

#         request = youtube.commentThreads().list(
#             part="snippet,replies",
#             videoId=video_id,
#             maxResults=100,
#             pageToken=next_page_token,
#             order="time",
#             textFormat="plainText"
#         )

#         response = request.execute()

#         for item in response.get("items", []):

#             # Top level comment
#             comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
#             comments.append(comment)

#             # Replies
#             if "replies" in item:
#                 for reply in item["replies"]["comments"]:
#                     reply_text = reply["snippet"]["textDisplay"]
#                     comments.append(reply_text)

#             if len(comments) >= max_comments:
#                 break

#         next_page_token = response.get("nextPageToken")

#         if not next_page_token or len(comments) >= max_comments:
#             break

#     print("Total comments fetched:", len(comments))

#     return comments
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
                maxResults=100,
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