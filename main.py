from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_yt_vid_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    video_id_list = query_params.get('v')

    if video_id_list:
        video_id = video_id_list[0]
        return video_id
    else:
        return "Video ID not found in the URL."

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([d["text"] for d in transcript])
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_summary(transcript):
    api_key = os.getenv('OPENROUTER_API_KEY')  # Replace with your actual API key
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "google/gemini-2.0-flash-exp:free",  # Optional; choose a model that you want to use
        "messages": [
            {
                "role": "user",
                "content": f"""
                    Answer the following questions and do the tasks based on the text below:
                    1. What is the type of information is being shared in the text?
                    2. Extract the summary of the text and sharekey points and learnings.
                    3. How can I use the idea to succeed in life?
                    
                    {transcript}               
                """
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()
    print(result.get("choices")[0].get("message").get("content"))

def main():
    url = "https://www.youtube.com/watch?v=DSrTS1_jhwE&t=1973s"
    # get the video id from the URL
    vid_id = get_yt_vid_id(url)
    print(f"Video ID: {vid_id}")
    # Get the video transcript
    transcript = get_transcript(vid_id)
    if transcript:
        # Get the summary of the transcript
        get_summary(transcript)
    else:
        print("Transcript not found.")

if __name__ == "__main__":
    main()