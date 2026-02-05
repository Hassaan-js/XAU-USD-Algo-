from typing import Dict, Optional

import pandas as pd

from strategy.base_strategy import BaseStrategy


class VSACABCISDStrategy(BaseStrategy):
    def __init__(
        self,
        vsa_rules: Optional[Dict[str, str]] = None,
        cab_rules: Optional[Dict[str, str]] = None,
        cisd_rules: Optional[Dict[str, str]] = None,
        timeframe: str = "1h",
    ) -> None:
        self.vsa_rules = vsa_rules or {}
        self.cab_rules = cab_rules or {}
        self.cisd_rules = cisd_rules or {}
        self.timeframe = timeframe

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError(
            "VSACABCISDStrategy needs explicit entry/exit rules before it can "
            "generate signals. Please fill in docs/strategy_requirements.md "
            "and then implement the signal logic here."
        )
