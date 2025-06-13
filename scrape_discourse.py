# scrape_discourse.py

import requests
import json
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_ID = 123  

def fetch_discourse_posts(start_date="2025-01-01", end_date="2025-04-14"):
    all_posts = []
    page = 0

    while True:
        url = f"{BASE_URL}/c/tools-in-data-science/{CATEGORY_ID}.json?page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        topics = data.get("topic_list", {}).get("topics", [])
        if not topics:
            break

        for topic in topics:
            created = topic.get("created_at", "")
            if start_date <= created[:10] <= end_date:
                all_posts.append(topic)

        page += 1

    with open("tds_discourse_posts.json", "w") as f:
        json.dump(all_posts, f, indent=2)

    print(f"Saved {len(all_posts)} posts.")

if __name__ == "__main__":
    fetch_discourse_posts()
