import ccxt
import pandas as pd
import time
from core.config import SYMBOL, TIMEFRAME, LIMIT, LIMIT1000


def get_ohlcv_spot(symbol="SEI/USDT", timeframe=TIMEFRAME, big_limit=LIMIT, limit=LIMIT1000):
    exchange = ccxt.binance()
    all_ohlcv = []
    since = None

    while True:
        print(f"Запрос с since={since}")
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit, since=since)

        if not ohlcv:
            print("Нет данных, выхожу")
            break

        # Добавляем в начало списка
        all_ohlcv = ohlcv + all_ohlcv

        # Проверяем, достаточно ли свечей
        if len(all_ohlcv) >= big_limit:
            break

        # Сдвигаем since на более старую дату
        oldest_timestamp = ohlcv[0][0]
        since = oldest_timestamp - (limit * 15 * 60 * 1000)  # 15 минут * 60 секунд * 1000 мс * лимит

        time.sleep(1)

    # Убираем дубликаты
    all_ohlcv = list({row[0]: row for row in all_ohlcv}.values())
    all_ohlcv.sort(key=lambda x: x[0])

    # Берём последние total_needed свечей
    all_ohlcv = all_ohlcv[-big_limit:]

    df = pd.DataFrame(
        all_ohlcv,
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df