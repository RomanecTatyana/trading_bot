from ta.momentum import RSIIndicator
from ta.trend import MACD, SMAIndicator
from ta.volatility import AverageTrueRange


# Розраховуємо індикатор RSI: беремо датафрейм, з нього серію close, розраховуємо індикатор, повертаємо серію з заголовком rsi, повертаємо датафрейм
def calc_rsi(df):
    try:
        rsi = RSIIndicator(df["close"]).rsi()
        df["rsi"] = rsi
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_rsi Error: {e}")
        

# Розрахоуємо індикатор MACD: беремо датафрейм, з нього серію close, розраховуємо індикатор, повертаємо серію з заголовком MACD_12_26, повертаємо датафрейм
def calc_macd(df):
    try:
        macd = MACD(df["close"])
        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_macd Error: {e}")
        
# Розраховуємо індикатор SMA: беремо датафрейм, з нього серію close, розраховуємо індикатор, повертаємо серію з заголовком sma_20, повертаємо датафрейм
def calc_sma(df):
    try:
        sma = SMAIndicator(df["close"], 20).sma_indicator()
        df["sma_20"]=sma
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_sma Error: {e}")
        
# Розраховуємо індикатор ATR щоб не входити на флетових ринках: беремо датафрейм, з нього серію High, Low, Close, період за замовчуванням 14, повертаємо серію з заголовком atr, повертаємо датафрейм
def calc_atr(df):
    try:
        atr = AverageTrueRange(df["high"], df["low"], df["close"]).average_true_range()
        df["atr"] = atr
        return df
    except Exception as e:
        print(f"strategies.indicators.py.calc_atr Error: {e}")
        
# Збираємо індикатори в одному датафреймі
def apply_all_indicator_spot(df):
    try:
        df = calc_rsi(df)
        df = calc_sma(df)
        df = calc_macd(df)
        df = calc_atr(df)
        return df
    except Exception as e:
        print(f"strategies.indicators.py.apply_all_indicator_spot Error: {e}")