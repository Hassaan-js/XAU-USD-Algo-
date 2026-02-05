import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file: str = "trading_system.log") -> logging.Logger:
    logger = logging.getLogger("trading_system")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
