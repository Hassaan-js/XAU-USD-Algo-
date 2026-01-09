import yaml
from data_handler.data_handler import DataHandler
from strategy.strategy_factory import StrategyFactory
from backtesting.backtester import BacktraderRunner
from monitoring.logging_config import setup_logging

def main():
    """
    The main entry point for the trading system.
    """
    # Set up logging
    logger = setup_logging()
    logger.info("Starting the trading system...")

    # Load configuration
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)
    logger.info("Configuration loaded successfully.")

    # Fetch data if it's not already cached
    data_handler = DataHandler(config['data_handler']['data_dir'])
    data_handler.get_data(
        ticker=config['data_handler']['ticker'],
        start_date=config['data_handler']['start_date'],
        end_date=config['data_handler']['end_date'],
        interval=config['data_handler']['interval']
    )

    # Get the strategy class from the factory
    strategy_name = config['strategy']['name']
    strategy_factory = StrategyFactory()
    strategy_class = strategy_factory.get_strategy_class(strategy_name)

    if not strategy_class:
        logger.error(f"Unknown strategy: {strategy_name}")
        return
    logger.info(f"Strategy selected: {strategy_name}")

    # Initialize and run the backtester
    backtester = BacktraderRunner(config)
    backtester.run_backtest(strategy_class)
    
    logger.info("Trading system finished.")

if __name__ == '__main__':
    main()
