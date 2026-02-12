import requests
import time
import os

print("Bot is starting...")

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

is_running = True
last_update_id = None

def send_message(text):
    print("Sending message:", text)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    print("Response:", response.text)

while True:
    if TOKEN and CHAT_ID:
        send_message("🚀 Bot is alive!")
    else:
        print("TOKEN or CHAT_ID missing!")

    time.sleep(60)
