from core.engine import run_bot
from core.data_loader import get_ohlcv

def run_bot():
    print("✅ Bot запущено — отримуємо дані...")
    df = get_ohlcv()
    df.to_csv("data/sei_usdt_1h.csv", index=False)
    print(f"Збережено {len(df)} свічок в data/sei_usdt_1h.csv")



if __name__ == "__main__":
    run_bot()



