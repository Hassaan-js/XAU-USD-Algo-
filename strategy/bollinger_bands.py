import pandas as pd

from strategy.base_strategy import BaseStrategy


class BollingerBandsStrategy(BaseStrategy):
    def __init__(self, bb_period: int, bb_std_dev: float) -> None:
        self.bb_period = bb_period
        self.bb_std_dev = bb_std_dev

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        signals = data.copy()
        rolling_mean = signals["Close"].rolling(window=self.bb_period)
        signals["bb_mid"] = rolling_mean.mean()
        rolling_std = signals["Close"].rolling(window=self.bb_period).std()
        signals["bb_upper"] = signals["bb_mid"] + (rolling_std * self.bb_std_dev)
        signals["bb_lower"] = signals["bb_mid"] - (rolling_std * self.bb_std_dev)

        signals["signal"] = 0
        signals.loc[signals["Close"] < signals["bb_lower"], "signal"] = 1
        signals.loc[signals["Close"] > signals["bb_upper"], "signal"] = -1
        return signals
