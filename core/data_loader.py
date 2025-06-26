import ccxt
import pandas as pd
from core.config import SYMBOL, TIMEFRAME, LIMIT


def get_ohlcv(symbol=SYMBOL, timeframe=TIMEFRAME, limit=LIMIT):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

