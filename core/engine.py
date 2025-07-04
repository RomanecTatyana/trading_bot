from core.data_loader import get_ohlcv_spot
from strategies.indicators import  calc_rsi, calc_macd
from strategies.rsi_macd import RSIMACDStrategy
from strategies.factory import get_strategy

def run_bot():
    print("✅ Bot запущено — отримуємо дані...")
    df = get_ohlcv_spot()
    df = calc_rsi(df)
    df = calc_macd(df)
    strategy = get_strategy("rsi_macd")
    df["signal"] = df.apply(strategy.generate_signal, axis=1)
    # df = apply_indicators(df)  # <-- Додаємо RSI и MACD
    
    df.to_csv("data/sei_usdt_1h.csv", index=False)
    print(df.tail(2500)[["close", "rsi", "macd", "macd_signal", "signal"]])

