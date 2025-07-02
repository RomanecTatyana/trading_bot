from trade import Trade

class Portfolio:
    def __init__(self, starting_balance):
        self.starting_balance = starting_balance
        self.free_balance = starting_balance
        self.open_trades = []
        self.closed_trades = []

    def open_trade(self, trade: Trade):
        investment = trade.entry_price * trade.quantity
        self.free_balance -= investment
        self.open_trades.append(trade)

    def close_trade(self, trade: Trade, exit_time, exit_price):
        trade.close(exit_time, exit_price)
        profit = trade.realized_pnl()
        self.free_balance += (trade.quantity * exit_price) + profit
        self.open_trades.remove(trade)
        self.closed_trades.append(trade)

    def total_balance(self, current_price_func):
        # Free balance + поточне значення всіх позицій
        invested_value = sum(
            t.quantity * current_price_func(t) for t in self.open_trades
        )
        return self.free_balance + invested_value
