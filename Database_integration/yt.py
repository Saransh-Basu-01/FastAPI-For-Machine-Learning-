# from fastapi import FastAPI
# import requests

# app = FastAPI()
# API_KEY = "AIzaSyCo2EWoomwLVygZ1LxhVV4KmL-iP4TH8sQ"  # Replace with your key

# @app.get("/influencers")
# def get_influencers(query: str = "clothing influencer"):
#     url = "https://www.googleapis.com/youtube/v3/search"
#     params = {
#         "part": "snippet",
#         "q": query,
#         "type": "channel",
#         "maxResults": 5,
#         "key": API_KEY
#     }
#     r = requests.get(url, params=params).json()
#     result = []
#     for item in r.get("items", []):
#         channel_id = item["snippet"]["channelId"]
#         channel_title = item["snippet"]["title"]
#         result.append({"channel_id": channel_id, "name": channel_title})
#     return result

from fastapi import FastAPI
import requests

app = FastAPI()
API_KEY = "AIzaSyCo2EWoomwLVygZ1LxhVV4KmL-iP4TH8sQ"  # Replace with your key

@app.get("/influencers")
def get_influencers(query: str = "clothing influencer"):
    # 1️⃣ Search channels
    search_url = "https://www.googleapis.com/youtube/v3/search"
    search_params = {
        "part": "snippet",
        "q": query,
        "type": "channel",
        "maxResults": 5,
        "key": API_KEY
    }
    search_res = requests.get(search_url, params=search_params).json()

    result = []
    for item in search_res.get("items", []):
        channel_id = item["snippet"]["channelId"]
        channel_name = item["snippet"]["title"]

        # 2️⃣ Fetch subscriber count
        stats_url = "https://www.googleapis.com/youtube/v3/channels"
        stats_params = {
            "part": "statistics",
            "id": channel_id,
            "key": API_KEY
        }
        stats_res = requests.get(stats_url, params=stats_params).json()
        subscribers = stats_res["items"][0]["statistics"].get("subscriberCount", "0")

        result.append({
            "channel_id": channel_id,
            "name": channel_name,
            "subscribers": subscribers
        })

    return result