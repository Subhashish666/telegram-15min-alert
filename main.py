import requests
import os
from datetime import datetime

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

now = datetime.now()
current_time = now.strftime("%H:%M")

# Since GitHub runs every 15 minutes,
# we just send message without checking minute
message = f"⏰ Time now: {current_time}"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": message}

response = requests.post(url, data=data)

print(response.text)
