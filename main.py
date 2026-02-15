import requests
import os
from datetime import datetime, timedelta

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Get UTC time from GitHub
utc_now = datetime.utcnow()

# Convert to India time (IST = UTC + 5:30)
ist_now = utc_now + timedelta(hours=5, minutes=30)

current_time = ist_now.strftime("%H:%M")

message = f"⏰ Time now: {current_time} IST"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": message}

response = requests.post(url, data=data)

print(response.text)
