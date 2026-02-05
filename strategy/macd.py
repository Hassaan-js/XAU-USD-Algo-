import pandas as pd

from strategy.base_strategy import BaseStrategy


class MACDStrategy(BaseStrategy):
    def __init__(self, fast_period: int, slow_period: int, signal_period: int) -> None:
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        signals = data.copy()
        exp1 = signals["Close"].ewm(span=self.fast_period, adjust=False).mean()
        exp2 = signals["Close"].ewm(span=self.slow_period, adjust=False).mean()
        signals["macd"] = exp1 - exp2
        signals["signal_line"] = signals["macd"].ewm(span=self.signal_period, adjust=False).mean()
        signals["signal"] = 0
        signals.loc[signals["macd"] > signals["signal_line"], "signal"] = 1
        signals.loc[signals["macd"] < signals["signal_line"], "signal"] = -1
        return signals
