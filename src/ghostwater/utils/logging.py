import logging
import sys


def get_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    logger.propagate = False
    return logger