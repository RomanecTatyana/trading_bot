from strategies.base import BaseStrategy

class RSIMACDStrategy(BaseStrategy):
    def __init__(self, rsi_buy=30, rsi_sell=70):
        self.rsi_buy = rsi_buy
        self.rsi_sell = rsi_sell

    def generate_signal(self, row):
        rsi = row.get("rsi")
        sma = row.get("sma_20")
        
        macd = row.get("macd")
        macd_signal = row.get("macd_signal")

        if rsi is None or macd is None or macd_signal is None:
            return "hold"

        if rsi < self.rsi_buy and macd > macd_signal:
            return "buy"
        elif rsi > self.rsi_sell and macd < macd_signal:
            return "sell"
        else:
            return "hold"
