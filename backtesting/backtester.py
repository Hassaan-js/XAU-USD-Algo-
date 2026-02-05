from dataclasses import dataclass
from typing import List, Type

import matplotlib.pyplot as plt
import pandas as pd

from data_handler.data_handler import DataHandler
from strategy.base_strategy import BaseStrategy


@dataclass
class Trade:
    entry_date: pd.Timestamp
    exit_date: pd.Timestamp
    entry_price: float
    exit_price: float
    direction: int
    pnl: float


class BacktraderRunner:
    def __init__(self, config: dict) -> None:
        self.config = config

    def run_backtest(self, strategy_class: Type[BaseStrategy]) -> None:
        data_cfg = self.config["data_handler"]
        strat_cfg = self.config["strategy"]
        risk_cfg = self.config["risk_management"]
        exec_cfg = self.config["execution_engine"]

        data_handler = DataHandler(data_cfg["data_dir"])
        data = data_handler.load_cached_data(
            ticker=data_cfg["ticker"],
            start_date=data_cfg["start_date"],
            end_date=data_cfg["end_date"],
            interval=data_cfg["interval"],
        )

        params = strat_cfg["parameters"].get(strat_cfg["name"], {})
        strategy = strategy_class(**params)
        signals = strategy.generate_signals(data).dropna().copy()

        cash = float(risk_cfg["total_initial_capital"])
        equity_curve = []
        position = 0
        entry_price = 0.0
        current_units = 0.0
        entry_date = None
        trades: List[Trade] = []

        for idx, row in signals.iterrows():
            price = float(row["Close"])
            signal = int(row["signal"])

            if position == 0 and signal != 0:
                risk_amount = cash * float(risk_cfg["risk_per_trade"])
                stop_loss_pct = float(risk_cfg["stop_loss_pct"])
                if stop_loss_pct <= 0:
                    continue
                position = signal
                entry_price = price * (1 + (exec_cfg["slippage"] * position))
                units = risk_amount / (entry_price * stop_loss_pct)
                cash -= units * exec_cfg["commission"]
                current_units = units
                entry_date = idx
            elif position != 0:
                take_profit = float(risk_cfg["take_profit_pct"])
                stop_loss = float(risk_cfg["stop_loss_pct"])
                price_change = (price - entry_price) / entry_price * position
                exit_trade = False

                if price_change <= -stop_loss or price_change >= take_profit:
                    exit_trade = True
                if signal == -position:
                    exit_trade = True

                if exit_trade:
                    exit_price = price * (1 - (exec_cfg["slippage"] * position))
                    pnl = (exit_price - entry_price) * position * current_units
                    cash += pnl
                    cash -= current_units * exec_cfg["commission"]
                    trades.append(
                        Trade(
                            entry_date=entry_date,
                            exit_date=idx,
                            entry_price=entry_price,
                            exit_price=exit_price,
                            direction=position,
                            pnl=pnl,
                        )
                    )
                    position = 0

            equity = cash
            if position != 0:
                equity += (price - entry_price) * position * current_units
            equity_curve.append({"Date": idx, "Equity": equity})

        equity_df = pd.DataFrame(equity_curve).set_index("Date")
        self._plot_equity_curve(equity_df)
        self._print_summary(trades, cash)

    def _plot_equity_curve(self, equity_df: pd.DataFrame) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(equity_df.index, equity_df["Equity"], label="Equity Curve")
        plt.title("Equity Curve")
        plt.xlabel("Date")
        plt.ylabel("Equity")
        plt.legend()
        plt.tight_layout()
        plt.savefig("equity_curve.png")
        plt.close()

    def _print_summary(self, trades: List[Trade], ending_cash: float) -> None:
        total_trades = len(trades)
        wins = sum(1 for trade in trades if trade.pnl > 0)
        win_rate = (wins / total_trades * 100) if total_trades else 0.0
        total_pnl = sum(trade.pnl for trade in trades)

        print("Backtest Summary")
        print("----------------")
        print(f"Total Trades: {total_trades}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"Total PnL: {total_pnl:.2f}")
        print(f"Ending Equity: {ending_cash:.2f}")
