import pandas as pd
import pandas_ta as ta

from strategy.base_strategy import BaseStrategy


class RSIMACrossoverStrategy(BaseStrategy):
    def __init__(
        self,
        rsi_period: int,
        rsi_buy_threshold: float,
        rsi_sell_threshold: float,
        short_ma_period: int,
        long_ma_period: int,
    ) -> None:
        self.rsi_period = rsi_period
        self.rsi_buy_threshold = rsi_buy_threshold
        self.rsi_sell_threshold = rsi_sell_threshold
        self.short_ma_period = short_ma_period
        self.long_ma_period = long_ma_period

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        signals = data.copy()
        signals["rsi"] = ta.rsi(signals["Close"], length=self.rsi_period)
        signals["short_ma"] = ta.sma(signals["Close"], length=self.short_ma_period)
        signals["long_ma"] = ta.sma(signals["Close"], length=self.long_ma_period)

        signals["signal"] = 0
        buy = (signals["rsi"] >= self.rsi_buy_threshold) & (signals["short_ma"] > signals["long_ma"])
        sell = (signals["rsi"] <= self.rsi_sell_threshold) & (signals["short_ma"] < signals["long_ma"])
        signals.loc[buy, "signal"] = 1
        signals.loc[sell, "signal"] = -1
        return signals
