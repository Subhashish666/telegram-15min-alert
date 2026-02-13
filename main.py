import requests
import time
import os
from datetime import datetime, timedelta

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
                    send_message("⏸ Notifications Paused")

                elif text == "/resume":
                    is_running = True
                    send_message("▶️ Notifications Resumed")


def wait_until_next_quarter():
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Calculate next 15-minute mark
    next_minute = (minutes // 15 + 1) * 15
    if next_minute == 60:
        next_time = now.replace(minute=0, second=0) + \
                    timedelta(hours=1)
    else:
        next_time = now.replace(minute=next_minute, second=0)

    wait_seconds = (next_time - now).total_seconds()
    time.sleep(wait_seconds)


while True:
    check_commands()

    if is_running:
        now = datetime.now()
        if now.minute % 15 == 0 and now.second == 0:
            send_message(f"⏰ Time now: {now.strftime('%H:%M')}")
            time.sleep(60)  # prevent duplicate sending

    time.sleep(1)
