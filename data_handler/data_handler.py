from pathlib import Path

import pandas as pd
import yfinance as yf


class DataHandler:
    def __init__(self, data_dir: str) -> None:
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, ticker: str, start_date: str, end_date: str, interval: str) -> Path:
        safe_ticker = ticker.replace("/", "_").replace("=", "_")
        filename = f"{safe_ticker}_{start_date}_{end_date}_{interval}.csv"
        return self.data_dir / filename

    def get_data(self, ticker: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
        cache_path = self._cache_path(ticker, start_date, end_date, interval)
        if cache_path.exists():
            return pd.read_csv(cache_path, parse_dates=["Date"], index_col="Date")

        data = yf.download(ticker, start=start_date, end=end_date, interval=interval, progress=False)
        if data.empty:
            raise ValueError(f"No data returned for {ticker} from {start_date} to {end_date} at {interval}.")

        data.reset_index(inplace=True)
        data.to_csv(cache_path, index=False)
        return data.set_index("Date")

    def load_cached_data(self, ticker: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
        cache_path = self._cache_path(ticker, start_date, end_date, interval)
        if not cache_path.exists():
            raise FileNotFoundError(f"Cached data not found at {cache_path}. Run get_data first.")
        return pd.read_csv(cache_path, parse_dates=["Date"], index_col="Date")
