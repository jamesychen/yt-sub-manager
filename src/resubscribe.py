from authenticate import get_authenticated_youtube
import json
import time
import os

def resubscribe_channels(youtube, max_subs=190):
    try:
        with open("data/unsubscribed_channels.json", "r", encoding="utf-8") as f:
            unsubscribed_channels = json.load(f)
    except FileNotFoundError:
        print("No 'data/unsubscribed_channels.json' file found. Run the unsubscribe script first.")
        return

    failed = []
    for i, sub in enumerate(unsubscribed_channels):
        if i >= max_subs:
            break
        try:
            youtube.subscriptions().insert(
                part="snippet",
                body={
                    "snippet": {
                        "resourceId": {
                            "kind": "youtube#channel",
                            "channelId": sub["channelId"]
                        }
                    }
                }
            ).execute()
            print(f"Resubscribed to: {sub['title']}")
        except Exception as e:
            print(f"Failed to resubscribe to {sub['title']}: {e}")
            failed.append(sub)
        time.sleep(2)

    if failed:
        with open("data/resubscribe_failed.json", "w", encoding="utf-8") as f:
            json.dump(failed, f, indent=4, ensure_ascii=False)
        print(f"\n{len(failed)} channels failed to resubscribe. Saved to 'data/resubscribe_failed.jso_
