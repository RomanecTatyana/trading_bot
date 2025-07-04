class Trade:
    def __init__(self, entry_time, entry_price, quantity):
        self.entry_time = entry_time
        self.entry_price = entry_price
        self.quantity = quantity
        self.exit_time = None
        self.exit_price = None

    def close(self, exit_time, exit_price):
        self.exit_time = exit_time
        self.exit_price = exit_price

    def realized_pnl(self):
        if self.exit_price is None:
            return 0.0
        return (self.exit_price - self.entry_price) * self.quantity

    def unrealized_pnl(self, current_price):
        return (current_price - self.entry_price) * self.quantity

    def is_open(self):
        return self.exit_price is None
