# Modular Algorithmic Trading System for XAU/USD

This project is a Python-based algorithmic trading system designed for the spot gold/USD (XAU/USD) market. It features a modular, object-oriented design that supports multiple strategy types, real-time data ingestion, and a robust backtesting engine.

## Core Features

- **Python-based & Object-Oriented:** Clean, maintainable, and extensible code.
- **Multiple Strategy Support:** Easily add and test new trading strategies. Comes with baseline strategies like RSI + Moving Average Crossover and Bollinger Bands.
- **Data Handling:** Fetches and manages historical price data from `yfinance`, with local caching for performance.
- **Backtesting Engine:** A powerful backtester to simulate strategies and evaluate performance with key metrics.
- **Risk Management:** Implements essential risk controls, including position sizing and stop-loss/take-profit logic.
- **Simulated Execution:** Models slippage and transaction costs for more realistic backtest results.
- **Comprehensive Logging:** Detailed logging of trades, system events, and errors for debugging and analysis.
- **Configurable:** All parameters are managed through a `config.yml` file, allowing for easy adjustments without code changes.

## Project Structure

The project is organized into the following modules:

- `data_handler/`: Manages the fetching, cleaning, and storage of market data.
- `strategy/`: Contains the trading strategy logic. New strategies can be added here.
- `risk_management/`: Handles risk controls, such as position sizing and stop-loss orders.
- `execution_engine/`: Simulates trade execution, including slippage and commissions.
- `backtesting/`: Orchestrates the backtesting process and calculates performance metrics.
- `monitoring/`: Provides logging and monitoring capabilities.
- `tests/`: Includes unit tests for critical functions.
- `main.py`: The main entry point for running the trading system.
- `config.yml`: The central configuration file for all parameters.
- `requirements.txt`: A list of all the necessary Python libraries.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

All parameters for the trading system are managed in the `config.yml` file. Before running a backtest, you can adjust the settings for the data, strategy, risk management, and execution to fit your needs.

-   **`data_handler`**: Set the ticker symbol, date range, and data interval.
-   **`strategy`**: Choose the strategy to backtest and configure its parameters.
-   **`risk_management`**: Define the risk per trade and the initial capital.
-   **`execution_engine`**: Specify the slippage and commission costs.

### Running a Backtest

To run a backtest with the settings defined in `config.yml`, simply execute the `main.py` script:

```bash
python main.py
```

The system will then:
1.  Fetch the historical data.
2.  Generate trading signals based on the selected strategy.
3.  Simulate the trades with the specified risk and execution parameters.
4.  Output the performance metrics to the console and log file.
5.  Save a plot of the equity curve as `equity_curve.png`.

## How to Add a New Strategy

The system is designed to be easily extensible. To add a new trading strategy, follow these steps:

1.  **Create a new Python file** in the `strategy/` directory (e.g., `my_strategy.py`).
2.  **Define a new class** that inherits from `BaseStrategy` (from `strategy.base_strategy`).
3.  **Implement the `generate_signals` method**, which takes historical data as input and returns a DataFrame with a `signal` column.
4.  **Update `main.py`** to include your new strategy as an option.
5.  **Add the configuration** for your new strategy to `config.yml`.

## Future Work

This project provides a solid foundation for a backtesting engine, but it is not yet a complete trading system. The following features are planned for future development:

-   **Real-Time Data Ingestion:** Integration with a broker API (e.g., OANDA, Interactive Brokers) to handle real-time data streams.
-   **Paper Trading Mode:** A simulated trading environment that uses real-time data to test strategies without risking capital.
-   **Live Execution Engine:** The ability to send and manage live orders with a brokerage.
-   **Advanced Risk Management:** Implementation of more sophisticated risk controls, such as maximum daily loss limits, drawdown monitoring, and position sizing based on volatility (e.g., ATR).
-   **Parameter Optimization:** A module for systematically testing a range of strategy parameters to find the optimal settings.
-   **Walk-Forward Analysis:** A more robust method of backtesting that helps to reduce the risk of curve-fitting.
-   **Performance Dashboard:** A more interactive dashboard for visualizing backtest results, using a library like Plotly.
