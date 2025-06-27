# strategies/base.py
class BaseStrategy:
    def generate_signal(self, row):
        raise NotImplementedError("Цю стратегію ще не реалізовано")
