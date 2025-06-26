from ta.momentum import RSIIndicator
from ta.trend import MACD


# Розраховуємо індикатор RSI: беремо датафрейм, з нього серію close, розраховуємо індикатор, повертаємо серію з заголовком rsi
def calc_rsi(df):
    try:
        rsi = RSIIndicator(df["close"]).rsi()
        df["rsi"] = rsi
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_rsi Error: {e}")
        

# Розрахоуємо індикатор MACD: беремо датафрейм, з нього серію close, розраховуємо індикатор, повертаємо серію з заголовком MACD_12_26
def calc_macd(df):
    try:
        macd = MACD(df["close"])
        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_macd Error: {e}")