from authenticate import get_authenticated_youtube
import json
import time
import os

def fetch_subscriptions(youtube):
    subscriptions = []
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)

    while request:
        response = request.execute()
        for item in response.get("items", []):
            subscriptions.append({
                "subscriptionId": item["id"],
                "channelId": item["snippet"]["resourceId"]["channelId"],
                "title": item["snippet"]["title"]
            })
        request = youtube.subscriptions().list_next(request, response)

    return subscriptions

def unsubscribe_channels(youtube, subscriptions, max_unsub=190):
    unsubscribed = []

    for i, sub in enumerate(subscriptions):
        if i >= max_unsub:
            break
        try:
            youtube.subscriptions().delete(id=sub["subscriptionId"]).execute()
            unsubscribed.append(sub)
            print(f"Unsubscribed from: {sub['title']}")
        except Exception as e:
            print(f"Failed to unsubscribe from {sub['title']}: {e}")
        time.sleep(2)

    os.makedirs("data", exist_ok=True)
    with open("data/unsubscribed_channels.json", "w", encoding="utf-8") as f:
        json.dump(unsubscribed, f, indent=4, ensure_ascii=False)

    print(f"\nUnsubscribed from {len(unsubscribed)} channels.")
    print("Saved to 'data/unsubscribed_channels.json'.")

youtube = get_authenticated_youtube()
subs = fetch_subscriptions(youtube)
unsubscribe_channels(youtube, subs)
