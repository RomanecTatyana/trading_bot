# strategies/factory.py
from strategies.rsi_macd import RSIMACDStrategy


def get_strategy(name: str):
    if name == "rsi_macd":
        return RSIMACDStrategy()
  
    else:
        raise ValueError(f"Невідома стратегія: {name}")
