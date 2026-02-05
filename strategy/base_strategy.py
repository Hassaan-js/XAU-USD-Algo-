from abc import ABC, abstractmethod

import pandas as pd


class BaseStrategy(ABC):
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Return a DataFrame with at least a 'signal' column of -1, 0, 1.
        """
        raise NotImplementedError
