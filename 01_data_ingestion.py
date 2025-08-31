import requests
import json
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Example channel (Google Developers)
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_youtube_data():
    params = {
        "part": "snippet",
        "channelId": CHANNEL_ID,
        "maxResults": 10,
        "order": "date",
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Save to Bronze Layer
    with open("../data/sample_raw.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("✅ Data fetched and stored in Bronze Layer")

if __name__ == "__main__":
    fetch_youtube_data()
