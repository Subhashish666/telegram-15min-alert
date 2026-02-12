import requests
import time
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

is_running = True
last_update_id = None

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def check_commands():
    global is_running, last_update_id

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url).json()

    for update in response.get("result", []):
        update_id = update["update_id"]

        if last_update_id is None or update_id > last_update_id:
            last_update_id = update_id

            if "message" in update:
                text = update["message"].get("text", "")

                if text == "/pause":
                    is_running = False
                    send_message("⏸ Alerts Paused")

                elif text == "/resume":
                    is_running = True
                    send_message("▶️ Alerts Resumed")

while True:
    check_commands()

    if is_running:
        send_message("⏰ 15 minutes passed")

    time.sleep(900)
