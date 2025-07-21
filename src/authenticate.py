from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CLIENT_SECRET_FILE = 'credentials/client_secret.json'

def get_authenticated_youtube():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=8080)
    youtube = build('youtube', 'v3', credentials=credentials)
    print("YouTube API client successfully authenticated!")
    return youtube
