import requests
import os
from datetime import datetime

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

now = datetime.now()
current_time = now.strftime("%H:%M")

# Send only at 00, 15, 30, 45
if now.minute % 15 == 0:
    message = f"⏰ Time now: {current_time}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    
    requests.post(url, data=data)
