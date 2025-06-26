import os
from datetime import datetime

def run_bot():
    os.makedirs("logs", exist_ok=True)
    with open("logs/bot.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] ✅ Bot запущено\n")
    print("✅ Bot запущено — лог записано.")
