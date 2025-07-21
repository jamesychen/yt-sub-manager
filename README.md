# 📺 YouTube Subscription Manager

Automate the management of your YouTube subscriptions using the **YouTube Data API v3**. This tool allows you to:

- 🔍 Fetch and export your current subscriptions  
- 🔄 Unsubscribe from all channels (in batches)  
- 🔁 Resubscribe from a saved list  

---

## 🚀 Features

- Fetch all current subscriptions and store them in a JSON file  
- Unsubscribe from all or selected channels using API calls  
- Restore your subscriptions later by re-running the resubscribe script  
- Supports batch operations and rate-limit handling  

---

## 🗂 Project Structure

youtube-subscription-manager/
│
├── src/
│ ├── fetch.py # Fetch current subscriptions
│ ├── unsubscribe.py # Unsubscribe from all saved channels
│ ├── resubscribe.py # Resubscribe to previously saved channels
│ └── utils/ # Helper functions (e.g., auth, API calls)
│
├── data/
│ ├── unsubscribed_channels.json # Backup of subscriptions
│
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/youtube-subscription-manager.git
   cd youtube-subscription-manager ```

2.Create a virtual environment and install dependencies
	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
	pip install -r requirements.txt
	```
3.Set up Google API credentials
	Go to Google Cloud Console
	Enable the YouTube Data API v3
	Create OAuth 2.0 credentials
	Download client_secret.json and place it in the root or src/ folder
	The script will handle token generation and refresh on first run
