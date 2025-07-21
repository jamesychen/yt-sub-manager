from authenticate import get_authenticated_youtube
import os

def save_channel_names(youtube):
    """
    Fetch YouTube channel names and save them to a text file.
    """
    channel_names = []
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)

    while request:
        response = request.execute()
        for item in response.get("items", []):
            channel_names.append(item["snippet"]["title"])

        request = youtube.subscriptions().list_next(request, response)

    if not channel_names:
        print("No subscriptions found.")
        return

    os.makedirs("data", exist_ok=True)
    with open("data/channel_names.txt", "w", encoding="utf-8") as f:
        for name in channel_names:
            print(name)
            f.write(name + "\n")

    print(f"\nFetched {len(channel_names)} channel names.")
    print("Saved to 'data/channel_names.txt'.")

youtube = get_authenticated_youtube()
save_channel_names(youtube)
