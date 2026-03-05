
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    """
    Extracts video ID from a YouTube URL.
    Works for:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    """
    parsed_url = urlparse(url)

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed_url.query)["v"][0]

    raise ValueError("Invalid YouTube URL")


def get_transcript(video_url: str):
    video_id = extract_video_id(video_url)

    transcript = YouTubeTranscriptApi() 

    chosen_transcript = transcript.list(video_id=video_id).find_transcript(["ja"]) 
    fetched_transcript = chosen_transcript.fetch() 

    full_text = ""
    for entry in fetched_transcript:
        full_text += entry.text 

    return full_text


## Enter this url for desired results : https://www.youtube.com/watch?v=dtAvmNUriDY (has proper japanese transcript) ## 

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")

    try:
        transcript_text = get_transcript(url)
        print(transcript_text)

    except Exception as e:
        print("Error:", e)




