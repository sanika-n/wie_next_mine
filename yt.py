from googleapiclient.discovery import build

#import openai

# Replace with your API Key from Google Cloud Console
YT_API_KEY = ''

# response = openai.completions.create(
#     model="gpt-4",  # or any other valid model
#     prompt="what are the important topics in python",
#     max_tokens=20
# )
# print("API key is valid. Response:", response['choices'][0]['text'])

youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

# Define the search query and parameters
query = "Python programming tutorials"
def yt_search(query):
    response = youtube.search().list(
        part="snippet",  # Specify the data parts to retrieve
        q=query,         # Search query
        type="video",    # Search only for videos
        maxResults=5     # Limit the number of results
    ).execute()

    # Process and print the search results
    for item in response.get("items", []):
        video_title = item["snippet"]["title"]
        channel_title = item["snippet"]["channelTitle"]
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"Title: {video_title}")
        print(f"Channel: {channel_title}")
        print(f"URL: {video_url}")
        print("-" * 40)
