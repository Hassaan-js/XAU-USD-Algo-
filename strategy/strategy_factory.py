from strategy.bollinger_bands import BollingerBandsStrategy
from strategy.macd import MACDStrategy
from strategy.rsi_ma_crossover import RSIMACrossoverStrategy
from strategy.vsa_cab_cisd import VSACABCISDStrategy


class StrategyFactory:
    def __init__(self) -> None:
        self._strategies = {
            "rsi_ma_crossover": RSIMACrossoverStrategy,
            "bollinger_bands": BollingerBandsStrategy,
            "macd": MACDStrategy,
            "vsa_cab_cisd": VSACABCISDStrategy,
        }

    def get_strategy_class(self, name: str):
        return self._strategies.get(name)
