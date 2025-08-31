import json
import pandas as pd

with open("../data/sample_raw.json", "r") as f:
    data = json.load(f)

items = data.get("items", [])
records = []
for item in items:
    snippet = item["snippet"]
    records.append({
        "videoId": item["id"].get("videoId"),
        "title": snippet.get("title"),
        "publishedAt": snippet.get("publishedAt"),
        "channelTitle": snippet.get("channelTitle")
    })

df = pd.DataFrame(records)
df.to_csv("../data/sample_silver.csv", index=False)
print("✅ Data transformed and stored in Silver Layer")
